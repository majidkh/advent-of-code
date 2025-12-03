use crate::helper::*;

pub fn part1() -> u32
{
    let mut joltage = 0;
    if let Ok(lines) = read_lines("src/input/3.txt") {
        for line in lines {
            if let Ok(text) = line {

                let digits: Vec<u32> = text
                    .chars()
                    .map(|c| c.to_digit(10).expect("non digit"))
                    .collect();

                joltage +=  find_jolt(digits);
            }
        }
    }

    joltage
}

pub fn part2() -> i32
{
    0
}

fn find_jolt ( bank : Vec<u32>) -> u32
{
    let mut jolt = 0;
    for i in 0..bank.len() -1
    {
        for j in i+1..bank.len()
        {
            let new = bank[i]* 10 + bank[j];
            if new > jolt{
                jolt = new;
            }
        }
    }


    jolt
}