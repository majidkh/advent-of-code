use crate::helper::*;
use regex::Regex;

pub fn part1() -> u64
{
    let mut numbers: Vec<Vec<u64>> = Vec::new();
    let mut operands: Vec<Vec<char>> = Vec::new();

    if let Ok(lines) = read_lines("src/input/6.txt") {
        for line in lines {
            if let Ok(text) = line {
                if text.len() > 0 {
                    // Ranges
                    if text.contains("+") || text.contains("*") {
                        let re = Regex::new(r"[+*]").unwrap();

                        let result: Vec<char> = re
                            .find_iter(&text)
                            .map(|m| m.as_str().parse::<char>().unwrap())
                            .collect();
                        operands.push(result);
                    }
                    else {
                        let re = Regex::new(r"\d+").unwrap();

                        let result: Vec<u64> = re
                            .find_iter(&text)
                            .map(|m| m.as_str().parse::<u64>().unwrap())
                            .collect();

                        if result.len() > 0 {
                            numbers.push(result);
                        }
                    }
                }
            }
        }
    }

    let mut sums = vec![0_u64; numbers[0].len()];
    for col in 0..numbers[0].len() {

        let op = operands[0][col];
        let mut res = numbers[0][col];
        for (row, inner) in numbers.iter().enumerate() {
            if row > 0 {
                if op == '+'{
                    res += inner[col];
                }
                else if op == '*'{
                    res *= inner[col];
                }
            }
        }
        sums[col] += res;
    }

    sums.iter().sum()
}

pub fn part2() -> u64
{
    0
}
