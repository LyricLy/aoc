use std::collections::HashMap;
use std::sync::{Mutex, OnceLock};
use std::iter;

type Memo = Mutex<HashMap<(Vec<usize>, Vec<Option<bool>>), usize>>;
fn memo() -> &'static Memo {
    static MEMO: OnceLock<Memo> = OnceLock::new();
    MEMO.get_or_init(|| Mutex::new(HashMap::new()))
}

fn meets_mask(p: impl Iterator<Item=bool>, mask: &[Option<bool>]) -> bool {
    p.zip(mask.iter()).all(|(a, b)| b.map(|b| a == b).unwrap_or(true))
}

fn places_meeting_mask(r: usize, mask: &[Option<bool>], at_end: bool) -> impl Iterator<Item=usize> + '_ {
    (0..(mask.len()+1).saturating_sub(r)).filter(move |&i| meets_mask(iter::repeat(false).take(i).chain(iter::repeat(true).take(r)).chain(iter::once(false).chain(iter::repeat(false).take_while(|_| at_end))), mask))
}

fn ways(p: Vec<usize>, mask: Vec<Option<bool>>) -> usize {
    if let Some(&r) = memo().lock().unwrap().get(&(p.clone(), mask.clone())) {
        return r;
    }
    let r = if p.len() == 1 {
        places_meeting_mask(p[0], &mask, true).count()
    } else {
        places_meeting_mask(p[0], &mask, false).map(|i| ways(p[1..].to_vec(), mask[(p[0] + i + 1).min(mask.len())..].to_vec())).sum()
    };
    memo().lock().unwrap().insert((p, mask), r);
    r
}

fn main() {
    let s = std::fs::read_to_string(std::env::args().nth(1).expect("provide filename")).unwrap();
    let mut c = 0;
    for line in s.lines() {
        let (x, y) = line.split_once(' ').unwrap();
        let p = y.split(',').map(|s| s.parse::<usize>().unwrap()).collect::<Vec<usize>>().repeat(5);
        let mut mask = x.chars().map(|x| if x == '.' { Some(false) } else if x == '#' { Some(true) } else { None }).collect::<Vec<Option<bool>>>();
        mask.push(None);
        let mut mask = mask.repeat(5);
        mask.pop();
        c += ways(p, mask);
    }
    println!("{c}");
}
