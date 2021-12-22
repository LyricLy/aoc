#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct LinkedList {
    int data;
    struct LinkedList *next;
};

typedef struct LinkedList * LL;


int main(int argc, char **argv) {
    if (argc < 2) {
        printf("you're dumb\n");
        return 0;
    }

    LL l = malloc(sizeof *l);
    LL end = malloc(sizeof *end);
    end->next = l;

    LL *things = malloc(sizeof *l * 1000000);

    char *ds = argv[1];
    int sl = strlen(argv[1]);
    for (int i = 0; i < 1000000; i++) {
        end = end->next;
        int next;
        if (i < sl) next = ds[i]-'0';
        else next = i+1;
        end->data = next;
        end->next = malloc(sizeof *end->next);
        things[next-1] = end;
    }
    free(end->next);
    end->next = l;

    for (int i = 0; i < 10000000; i++) {
        LL p = l->next;
        l->next = l->next->next->next->next;
        p->next->next->next = NULL;

        int s = l->data-1;
        if (s < 1) s = 1000000;
        for (;;) {
            LL thing = things[s-1];
            if (thing->data == p->data || thing->data == p->next->data || thing->data == p->next->next->data) {
                s--;
                if (s < 1) s = 1000000;
            } else {
                p->next->next->next = thing->next;
                thing->next = p;
                if (s == end->data) end = p->next->next;
                break;
            }
        }

        end->next->data = l->data;
        end->next->next = l->next;
        end = end->next;
        l = l->next;
    }

    while (l->data != 1) {
        l = l->next;
    }
    printf("%d * %d = %lld\n", l->next->data, l->next->next->data, (long long) l->next->data * l->next->next->data);
}
