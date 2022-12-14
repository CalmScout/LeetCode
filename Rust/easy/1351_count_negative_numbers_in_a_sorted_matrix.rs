// Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
// Return the number of negative numbers in grid.

impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut count: i32 = 0;
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j] < 0 {
                    count += 1;
                }
            }
        }
        count
    }
}