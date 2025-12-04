use crate::helper::*;

pub fn part1() -> i32
{
    let mut counter = 0;

    if let Ok(lines) = read_lines("src/input/4.txt") {

        let grid: Vec<Vec<char>> = lines
            .filter_map(Result::ok)       // ignore lines that failed to read
            .map(|line| line.chars().collect())
            .collect();

        let grid_copy = grid.clone();

        for (i,row) in grid.iter().enumerate() {
            for (j, _value) in row.iter().enumerate() {
                if grid[i][j] == '@' {
                    if count(&grid_copy, i as i32, j as i32) < 4
                    {
                        counter += 1;
                    }
                }
            }
        }
    }

    counter
}

pub fn part2() -> i32
{
    let mut counter = 0;

    if let Ok(lines) = read_lines("src/input/4.txt") {

        let grid: Vec<Vec<char>> = lines
            .filter_map(Result::ok)       // ignore lines that failed to read
            .map(|line| line.chars().collect())
            .collect();

        let mut grid_copy = grid.clone();
        let mut found = true;

        while found
        {
            found = false;
            for (i, row) in grid.iter().enumerate() {
                for (j, _value) in row.iter().enumerate() {
                    if grid_copy[i][j] == '@' {
                        if count(&grid_copy, i as i32, j as i32) < 4
                        {
                            counter += 1;
                            found = true;
                            grid_copy[i][j] = 'x';
                        }
                    }
                }
            }
        }
    }

    counter
}


fn count ( grid : &Vec<Vec<char>>, row: i32, col : i32 ) -> i32
{
    let adjacent: Vec<(isize, isize)> = vec![
        (-1, -1), // top-left
        (0, -1),  // top
        (1, -1),  // top-right
        (-1, 0),  // left
        (1, 0),   // right
        (-1, 1),  // bottom-left
        (0, 1),   // bottom
        (1, 1),   // bottom-right
    ];

    let mut count = 0;

    for pos in adjacent
    {
        if has_paper(grid , row + pos.0 as i32 , col + pos.1 as i32 )
        {
            count += 1;
        }

    }

    count
}

fn has_paper( grid : &Vec<Vec<char>>, row: i32, col :i32 )-> bool
{
    if col < 0 || row < 0
    {
        return false;
    }

    if row >= grid.len() as i32 || col >= grid[0].len() as i32
    {
        return false;
    }

    if grid[row as usize][col as usize] == '@' { true } else { false }
}