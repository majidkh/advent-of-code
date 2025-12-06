use crate::helper::*;
use regex::Regex;

pub fn part1() -> u64
{
    let (numbers,operands) = parse_input();
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
    // Calculate column widths
    let (tmp_numbers,operands) = parse_input();
    let mut column_widths = vec![0_usize; tmp_numbers[0].len()];
    for col in 0..column_widths.len() {
        for nums in tmp_numbers.iter(){
            if nums[col].to_string().len() > column_widths[col] {
                column_widths[col] = nums[col].to_string().len();
            }
        }
    }
    let str_numbers= parse_input_with_padding( &column_widths);
    let mut sums = vec![0_u64; str_numbers[0].len()];
    for col in 0..str_numbers[0].len() {
        let op = operands[0][col];
        let mut res = 0;
        for digit_no in (0..column_widths[col]).rev() {
            let mut str_num: String = String::new();
            for inner in str_numbers.iter() {
                let char = inner[col].chars().nth(digit_no).unwrap().to_string();
                if !char.eq("0") {
                    str_num.push_str(char.as_str());
                }
            }
            let num = str_num.parse::<u64>().unwrap();
            if res == 0 {
                res = num;
            } else {
                if op == '+' {
                    res += num;
                } else if op == '*' {
                    res *= num;
                }
            }
        }
        sums[col] += res;
    }
    sums.iter().sum()
}

fn parse_input() -> (Vec<Vec<u64>>, Vec<Vec<char>>) {
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
    (numbers, operands)
}

fn parse_input_with_padding( col_widths: &Vec<usize>) -> Vec<Vec<String>> {
    let mut str_numbers: Vec<Vec<String>> = Vec::new();
    if let Ok(lines) = read_lines("src/input/6.txt") {
        for line in lines {
            if let Ok(text) = line {
                if text.len() > 0 {
                    let mut index = 0;
                    if ! text.contains("+") && ! text.contains("*") {
                        let mut result: Vec<String> = Vec::new();
                        for col in 0..col_widths.len() {
                            let num: String = text.chars().skip(index).take( col_widths[col]).collect();
                            index += num.len()+1;
                            result.push ( num.replace(" ","0"));
                        }
                        str_numbers.push(result);
                    }
                }
            }
        }
    }
    str_numbers
}