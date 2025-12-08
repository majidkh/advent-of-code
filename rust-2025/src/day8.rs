use std::collections::{HashSet};
use crate::helper::*;
pub fn part1() -> usize
{
    get_nodes(10)
}

pub fn part2() -> i64
{
    0
}

fn get_nodes( connections: i32 ) -> usize
{
    // Extract junctions
    let mut junctions:Vec<(i64,i64,i64)> = Vec::new();
    if let Ok(lines) = read_lines("src/input/8.txt") {
        for line in lines {
            if let Ok(text) = line {
                let parts: Vec<i64> = text.split(",").map(|s| s.trim().parse::<i64>().unwrap())
                    .collect();
                junctions.push((parts[0], parts[1], parts[2]));
            }
        }
    }

    // calculate distances between pairs
    let mut circuits :Vec<Vec<usize>> = Vec::new();
    let mut pairs:Vec<((usize, usize), f64)> = Vec::new();
    let mut cache: HashSet<(usize, usize)> = HashSet::new();

    for (i1 , junction1) in junctions.iter().enumerate() {
        for (i2, junction2) in junctions.iter().enumerate() {
            if i1 == i2{
                continue;
            }

            let d = distance(*junction1, *junction2);
            let mut pair = (i1,i2);
            if i1 > i2{
                pair = (i2,i1);

            }

            if ! cache.contains(&pair)
            {
                pairs.push((pair, d));
                cache.insert(pair);
            }
        }
    }

    pairs.sort_by(|a, b| a.1.partial_cmp(&b.1).unwrap());
    // Now connect the circuits

    let mut added = 0;

    'outer: for pair in pairs.iter()
    {
        // Check for existing circuits for any of the new connecting pairs
        let mut existing:Vec<usize> = Vec::new();
        for (i,c) in circuits.iter().enumerate(){
            if c.contains( &pair.0.0) && c.contains(&pair.0.1){
                // Directly connected
                added += 1;
                continue 'outer;
            }
            if c.contains( &pair.0.0) || c.contains(&pair.0.1){
                existing.push(i);
            }
        }
        added += 1;

        // If no circuit contains them, create a new circuit
        if existing.len() == 0{
            circuits.push( vec![pair.0.0, pair.0.1] );
        }
        else if existing.len() == 1 {
            // If one of the pairs is connected, connect the second pair

            if circuits[ existing[0]].contains( &pair.0.0){
                circuits[ existing[0]].push(pair.0.1);
            }
            else if circuits[ existing[0]].contains( &pair.0.1){
                circuits[ existing[0]].push(pair.0.0);
            }
        }
        else if existing.len() == 2 {
            // If both pairs exist in different circuits , merge them together
            let c1 = circuits[ existing[0]].clone();
            circuits[existing[1]].append(&mut c1.clone());
            circuits.remove( existing[0] );
        }

        if added >= connections{
            break 'outer;
        }
    }

    circuits.sort_by(|a, b| b.len().cmp(&a.len()));
    circuits[0].len() * circuits[1].len() * circuits[2].len()
}

fn distance(a: (i64, i64, i64), b: (i64, i64, i64)) -> f64 {

    let dx = b.0 - a.0;
    let dy = b.1 - a.1;
    let dz = b.2 - a.2;
    let q = (dx * dx + dy * dy + dz * dz).abs() as f64;
    q.sqrt()
}