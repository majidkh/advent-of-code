use crate::helper::*;

pub fn part1() -> i64
{
    let mut best = 0;
    if let Ok(lines) = read_lines("src/input/3.txt") {
        for line in lines {
            if let Ok(text) = line {
                let digits: Vec<u32> = text
                    .chars()
                    .map(|c| c.to_digit(10).expect("non digit"))
                    .collect();

                best +=  find_jolt(digits , 2 , 0 , 0);
            }
        }
    }
    best
}

pub fn part2() -> i64
{
    let mut best = 0;
    if let Ok(lines) = read_lines("src/input/3.txt") {
        for line in lines {
            if let Ok(text) = line {

                let digits: Vec<u32> = text
                    .chars()
                    .map(|c| c.to_digit(10).expect("non digit"))
                    .collect();

                best +=  find_jolt(digits , 12 , 0 , 0);
            }
        }
    }
    best
}

fn find_jolt ( bank : Vec<u32> , mut depth : usize , value : i64, mut best: i64) -> i64
{
    depth -= 1;

    let max_value_i32 = *bank[0..bank.len() - depth].iter().max().unwrap(); // i32
    let max_value_u32 = max_value_i32 as u32;     // cast to u32

    for i in 0..bank.len() - depth
    {
        if bank[i] == max_value_u32
        {
            let jolt = bank[i] as i64 * 10i64.pow(depth as u32);
            if depth >= 1 && bank.len() > 0
            {
                let new = find_jolt(bank[i + 1..].to_vec(), depth, value + jolt, best);
                if new > best {
                    best = new;
                }
            } else {
                if value + bank[i] as i64 > best {
                    return value + bank[i] as i64;
                }
            }
        }
    }

    best
}