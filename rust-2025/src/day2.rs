use crate::helper::*;
pub fn part1() -> i64
{
    let mut invalids = 0;
    if let Ok(contents) = read_contents("src/input/2.txt") {
        let text = contents.replace("\r", " ").replace("\n", "");
        let ranges: Vec<&str> = text.split(',').collect();
        for range in ranges {
            let parts:Vec<&str> = range.split("-").collect();
            let first: i64 = parts[0].parse().expect("Failed to parse first number");
            let second: i64 = parts[1].parse().expect("Failed to parse second number");

            invalids += find_invalids(first, second);
        }
    }
    invalids
}

pub fn part2() -> i32
{
    0
}

fn find_invalids( from :i64 , to:i64 ) -> i64
{
    let mut c = 0;
    for i in from..=to {
        let str_i = i.to_string();
        let str_len = str_i.len();
        if str_len % 2 == 0{

            let first_half: String = str_i.chars().take(str_len / 2).collect();
            let second_half: String = str_i.chars().skip(str_len / 2).collect();

            if first_half == second_half {
                c +=i;
            }
        }
    }

    c
}