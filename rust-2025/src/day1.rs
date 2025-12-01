use crate::helper::read_lines;

pub fn part1() -> i32
{
    count_passwords(false)
}

pub fn part2() -> i32
{
    count_passwords(true)
}

fn count_passwords( passes : bool )-> i32
{
    let mut dial = 50;
    let mut last_dial = 50;
    let mut password = 0;

    if let Ok(lines) = read_lines("src/1.txt") {
        for line in lines {
            if let Ok(text) = line {
                let dir = text.chars().next().unwrap();
                let s_val: String = text.chars().skip(1).collect();
                let mut val = s_val.parse::<i32>().unwrap();
                // Full rounds
                if val.abs() / 100 > 0 {
                    let rounds = val.abs() / 100;

                    if passes {
                        password += rounds;
                    }
                    val = val - rounds * 100;
                }

                if dir == 'L' {
                    dial -= val;

                    if dial < 0
                    {
                        if last_dial != 0 && passes {
                            password += 1;
                        }
                        dial += 100;
                    }
                    last_dial = dial;
                }
                else if dir == 'R'
                {
                    dial += val;
                    if dial > 99{
                        dial -= 100;
                        if dial != 0 && passes {
                            password += 1;
                        }
                    }
                    last_dial = dial;
                }

                if dial == 0{
                    password += 1;
                }
            }
        }
    }

    password
}