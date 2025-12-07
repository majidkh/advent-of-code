use crate::helper::*;

pub fn part1() -> usize
{
    let grid = read_grid();
    let mut manifold = read_grid();
    let mut split = 0;

    for (row,line) in grid.iter().enumerate()
    {
        for (col,loc) in line.iter().enumerate() {
            if *loc == 'S' || manifold[row][col] == '|'
            {
                move_beam(col,row , & mut manifold , & mut split);

                if row < grid.len() -1{
                    if manifold[row+1][col] == '.'{
                        manifold[row+1][col] = '|';
                    }
                }
            }
        }
    }

    split
}

pub fn part2() -> u64
{
    0
}

fn read_grid() -> Vec<Vec<char>>
{
    let mut grid:Vec<Vec<char>> = Vec::new();
    if let Ok(lines) = read_lines("src/input/7.txt") {
        for line in lines {
            if let Ok(text) = line {
                grid.push(text.chars().collect());

            }
        }
    }

    grid
}

fn move_beam( col:usize , row:usize , manifold:&mut Vec<Vec<char>> , split: &mut usize )
{
    if row < manifold.len() -1{
        if manifold[row+1][col] == '.'{
            manifold[row+1][col] = '|';
            move_beam( col ,row +1 ,manifold , split );
        }
        if manifold[row+1][col] == '^'{
            if row < manifold.len()-2{
                if manifold[row+2][col-1] == '.' || manifold[row+2][col+1] == '.'{
                    *split += 1;
                }
            }
            move_beam( col -1 ,row +1 ,manifold , split );
            move_beam( col +1 ,row +1 ,manifold , split );
        }
    }
}