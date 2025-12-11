use std::collections::{HashSet, VecDeque};
use regex::Regex;
use crate::helper::*;
pub fn part1() -> u32
{
    let machines = get_machines();
    let mut total = 0;
    for machine in machines {
        let res = part1_calculate(&machine.0, &machine.1);
        total += res;
    }
    total
}

pub fn part2() -> i64
{
    0
}

fn part1_calculate( target: &Vec<u8> , buttons: &Vec<Vec<u8>> ) -> u32
{
    let current:Vec<u8> = vec![0; target.len()];
    let mut queue: VecDeque<(u32, Vec<u8>, usize)> = VecDeque::new();
    let mut cache:HashSet<Vec<u8>> = HashSet::new();

    for (index,b) in buttons.iter().enumerate() {
        // If first button press results the target
        if b.eq(target) {
            return 1;
        }

        queue.push_back((1, current.clone(), index));
    }
    cache.insert(current.clone());

    while let Some((c, s, index)) = queue.pop_front() {
       let result = press (s,&buttons[index] );
        if !cache.contains(&result) {
            cache.insert(result.clone());
            if &result == target {
                return c;
            }

            for i in 0..buttons.len() {
                if i != index {
                    queue.push_back((c + 1, result.clone(), i));
                }
            }
        }
    }
    0
}

fn press (mut val:Vec<u8> , button:&Vec<u8> ) -> Vec<u8>
{
    for i in 0..button.len() {
        val[i] = val[i]  ^ button[i]
    }
    val
}

fn get_machines() -> Vec<(Vec<u8> , Vec<Vec<u8>> , Vec<u32> )>
{
    let mut machines: Vec<(Vec<u8>, Vec<Vec<u8>>, Vec<u32>)> = Vec::new();

    // Extract junctions
    if let Ok(lines) = read_lines("src/input/10.txt") {
        for line in lines {
            if let Ok(text) = line {
                let mut diagram: Vec<u8> = Vec::new();
                // Extract the Diagram
                let re = Regex::new(r"\[([.#]+)]").unwrap();
                for caps in re.captures_iter(text.as_str()) {
                    for c in caps[1].chars() {
                        if c == '#'{
                            diagram.push(1);
                        }
                        else {
                            diagram.push(0);
                        }
                    }
                }

                // Extract the schematics
                let mut buttons: Vec<Vec<u8>> = Vec::new();
                let re = Regex::new(r"\(([\d, ]+)\)").unwrap();
                for caps in re.captures_iter(text.as_str()) {
                    let nums = caps[1].split(",").map(|x| x.parse::<usize>().unwrap()).collect::<Vec<usize>>();

                    let mut button: Vec<u8> = vec![0; diagram.len()];
                    for n in nums {
                        button[n] = 1;
                    }
                    buttons.push(button);
                }

                // Extract the joltage
                let mut joltage: Vec<u32> = Vec::new();
                let re = Regex::new(r"\{([\d, ]+)}").unwrap();
                for caps in re.captures_iter(text.as_str()) {
                    for c in caps[1].split(",") {
                        joltage.push(c.parse::<u32>().unwrap());
                    }
                }
                machines.push(( diagram, buttons, joltage));
            }
        }
    }
    machines
}
