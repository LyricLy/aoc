#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}

int main() {
    FILE *fp = fopen("input.txt", "r");
    int n;
    int count = 0;
    while (fscanf(fp, "%d", &n) != EOF) count++;
    fseek(fp, 0, SEEK_SET);

    int *adaptors = malloc((count+1) * sizeof (int));
    int max = -1;
    for (int i = 0; i < count; i++) {
        fscanf(fp, "%d", &n);
        adaptors[i] = n;
        if (n > max) max = n;
    }
    fclose(fp);
    adaptors[count] = 0;
    count += 1;
    qsort(adaptors, count, sizeof *adaptors, cmp);

    long long *paths_to = calloc(max+7, sizeof (long long));
    paths_to[0] = 1;
    for (int i = 0; i < count; i++) {
        printf("%d %lld\n", adaptors[i], paths_to[adaptors[i]]);
        for (int j = 1; j <= 3; j++) {
            paths_to[adaptors[i]+j] += paths_to[adaptors[i]];
        }
    }

    printf("%lld\n", paths_to[adaptors[count-1]]);
}
