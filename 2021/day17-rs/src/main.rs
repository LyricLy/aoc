#![feature(test)]

extern crate test;

use core::ops::Range;
use test::bench::Bencher;

struct Input {
    x: Range<i32>,
    y: Range<i32>,
}

struct Counts<const TIMES: usize, const REPEATS: usize> {
    times: [u32; TIMES],
    repeats: [[u8; REPEATS]; TIMES],
    beyonds: u32,
}

struct RepeatQueue<const REPEATS: usize> {
    d: [bool; REPEATS],
}

impl<const REPEATS: usize> RepeatQueue<REPEATS> {
    #[inline(always)]
    fn new() -> Self {
        RepeatQueue { d: [false; REPEATS] }
    }

    #[inline(always)]
    fn push(&mut self, v: bool) {
        let mut to_push = std::mem::replace(&mut self.d[0], v);
        for i in 1..REPEATS {
            std::mem::swap(&mut self.d[i], &mut to_push);
        }
    }
}

fn get_counts<const TIMES: usize, const REPEATS: usize>(y: Range<i32>) -> Counts<TIMES, REPEATS> {
    let mut times = [0; TIMES];
    let mut repeats = [[0; REPEATS]; TIMES];
    let mut beyonds = 0;
    for oy in y.start..-y.start {
        let mut v = oy;
        let s = if v > 0 {
            let r = (v*2+1) as usize;
            v = !v;
            r
        } else {
            0
        };
        let mut i = 0;
        let mut repeat = RepeatQueue::<REPEATS>::new();
        for time in s.. {
            let contained = y.contains(&i);
            if contained {
                if time < TIMES {
                    for j in 0..REPEATS {
                        if repeat.d[j] {
                            repeats[time][j] += 1;
                            break;
                        }
                    }
                    times[time] += 1;
                } else {
                    beyonds += 1;
                    break;
                }
            }
            if i < y.start {
                break;
            }
            repeat.push(contained);
            i += v;
            v -= 1;
        }
    }
    dbg!(times, repeats, beyonds);
    Counts { times, repeats, beyonds }
}

fn use_counts<const TIMES: usize, const REPEATS: usize>(x: Range<i32>, counts: Counts<TIMES, REPEATS>) -> u32 {
    let mut count = 0;
    for ox in 1..x.end {
        let mut v = ox;
        let mut i = 0;
        let mut repeat = RepeatQueue::<REPEATS>::new();
        let mut ever_contained = false;
        for time in 0..TIMES {
            let contained = x.contains(&i);
            if contained {
                ever_contained = true;
                count += counts.times[time];
                for j in 0..REPEATS {
                    if repeat.d[j] {
                        count -= counts.repeats[time][j] as u32;
                    }
                }
            }
            if i >= x.end { break; }
            repeat.push(contained);
            i += v;
            if v != 0 { v -= 1; }
        }
        if v == 0 && ever_contained {
            count += counts.beyonds;
        }
    }
    count
}

fn part2(inp: &Input) -> u32 {
    let counts = get_counts::<64, 1>(inp.y.clone());
    use_counts(inp.x.clone(), counts)
}

#[bench]
fn bench(b: &mut Bencher) {
    let input = &Input { x: 119..177, y: -141..-83 };
    b.iter(|| test::black_box(part2(input)));
}

#[bench]
fn bench_get_counts(b: &mut Bencher) {
    let input = &Input { x: 119..177, y: -141..-83 };
    b.iter(|| test::black_box(get_counts::<64, 1>(input.y.clone())));
}

fn main() {
    let input = &Input { x: 119..177, y: -141..-83 };
    let example = &Input { x: 20..31, y: -10..-4 };
    dbg!(part2(input));
}
