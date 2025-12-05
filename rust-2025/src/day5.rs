use crate::helper::*;

pub fn part1() -> i32
{
    let mut ranges: Vec<[u64; 2]> = Vec::new();
    let mut ingredients:Vec<u64> = Vec::new();
    if let Ok(lines) = read_lines("src/input/5.txt") {
        for line in lines {
            if let Ok(text) = line {
               if text.len() > 0 {
                   // Ranges
                   if text.contains('-') {
                       let parts: Vec<u64> = text
                           .split('-')
                           .map(|s| s.parse::<u64>().unwrap())
                           .collect();
                        ranges.push ([parts[0], parts[1]]);
                   } else {
                       // Ingredients
                       ingredients.push(text.parse::<i64>().unwrap() as u64);
                   }
               }

            }
        }
    }

    let mut fresh = 0;
    for i in ingredients.iter() {
        if is_fresh( *i, &ranges) {
            fresh += 1;
        }
    }

    fresh
}

pub fn part2() -> i32
{
    0
}

fn is_fresh (id: u64, range: &Vec<[u64; 2]>) -> bool
{
    for (i, &[r1, r2]) in range.iter().enumerate() {
        if id >= r1 && id <= r2 {
            return true
        }
    }
    false
}