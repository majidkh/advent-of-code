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

pub fn part2() -> u64
{
    let mut fresh_ids = 0;

    let mut ranges: Vec<[u64; 2]> = Vec::new();
    if let Ok(lines) = read_lines("src/input/5.txt") {
        for line in lines {
            if let Ok(text) = line {
                if text.len() > 0 {
                    // Ranges
                    if text.contains('-') {
                        let mut parts: Vec<u64> = text
                            .split('-')
                            .map(|s| s.parse::<u64>().unwrap())
                            .collect();

                        let mut new_parts = parts.clone();
                        let mut split = false;
                        // Count unique ranges
                        for  &[r1, r2] in ranges.iter()
                        {
                            if parts[0] >= r1 && parts[0] <= r2 {
                                parts[0] = r2 + 1
                            }
                            if parts[1] >= r1 && parts[1] <= r2 {
                                parts[1] = r1 - 1;
                            }

                            // if needs splitting
                            if parts[0] < r1 && parts[1] > r2 {
                                new_parts[0] = r2 + 1;

                                parts[1] = r1 - 1;
                                split = true;
                            }
                        }

                        if parts[1] >= parts[0] {
                            ranges.push([parts[0], parts[1]]);
                            if split{
                                ranges.push([new_parts[0], new_parts[1]]);
                            }
                        }
                    }
                }
            }
        }
    }

    for  &[ n1, n2] in ranges.iter(){
        fresh_ids += n2 - n1 + 1;
    }

    fresh_ids
}

fn is_fresh (id: u64, range: &Vec<[u64; 2]>) -> bool
{
    for &[r1, r2] in range.iter() {
        if id >= r1 && id <= r2 {
            return true
        }
    }
    false
}