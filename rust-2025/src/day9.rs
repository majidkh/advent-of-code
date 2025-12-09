use crate::helper::*;
pub fn part1() -> u64
{
    let tiles = get_tiles();
    let mut max = 0;
    for t1 in tiles.iter(){
        for t2 in tiles.iter(){
            if t1 != t2{
                let area = ( t1.0.abs_diff(t2.0) + 1 ) * ( t1.1.abs_diff(t2.1) + 1 ) ;
                if area > max{
                    max = area;
                }

            }
        }
    }
    max
}

pub fn part2() -> i64
{
    0
}

fn get_tiles() -> Vec<(u64,u64)>
{
    let mut tiles: Vec<(u64,u64)> = Vec::new();
    // Extract junctions
    if let Ok(lines) = read_lines("src/input/9.txt") {
        for line in lines {
            if let Ok(text) = line {
                let parts: Vec<u64> = text.split(",").map(|s| s.trim().parse::<u64>().unwrap())
                    .collect();
                tiles.push((parts[0], parts[1]));
            }
        }
    }
    tiles
}