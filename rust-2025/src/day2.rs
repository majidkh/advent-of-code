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

            invalids += find_invalids(first, second , false );
        }
    }
    invalids
}

pub fn part2() -> i64
{
    let mut invalids = 0;
    if let Ok(contents) = read_contents("src/input/2.txt") {
        let text = contents.replace("\r", " ").replace("\n", "");
        let ranges: Vec<&str> = text.split(',').collect();
        for range in ranges {
            let parts:Vec<&str> = range.split("-").collect();
            let first: i64 = parts[0].parse().expect("Failed to parse first number");
            let second: i64 = parts[1].parse().expect("Failed to parse second number");

            invalids += find_invalids(first, second , true );
        }
    }
    invalids
}

fn find_invalids( from :i64 , to:i64, repeat:bool ) -> i64
{
    let mut c = 0;
    for i in from..=to {
        let str_i = i.to_string();
        let str_len = str_i.len();
        if repeat {
            if is_invalid(str_i , 0 , str_len/2) {
                c += i
            }
        }
        else {
            if str_len % 2 == 0 && is_invalid(str_i , (str_len/2)-1 , str_len/2 ) {
                c += i
            }
        }
    }
    c
}

fn is_invalid ( number: String , from: usize , to: usize ) -> bool
{
    let str_len = number.len();
    for i in from..to{
        let r = number.chars().take(i + 1).collect::<String>().repeat(str_len/(i+1) );
        if r == number{
            return true
        }
    }
    false
}