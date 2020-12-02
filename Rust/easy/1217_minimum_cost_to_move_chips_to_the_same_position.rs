// We have n chips, where the position of the ith chip is position[i].

// We need to move all the chips to the same position. In one step, we
// can change the position of the ith chip from position[i] to:

// position[i] + 2 or position[i] - 2 with cost = 0.
// position[i] + 1 or position[i] - 1 with cost = 1.
// Return the minimum cost needed to move all the chips to the same
// position.
use std::cmp;

impl Solution {
    pub fn min_cost_to_move_chips(position: Vec<i32>) -> i32 {
        let mut even_count: i32 = 0;
        let mut odd_count: i32 = 0;
        for idx in 0..position.len() {
            if position[idx] % 2 == 0 {
                even_count += 1;
            } else {
                odd_count += 1;
            }
        }
        return cmp::min(even_count, odd_count)
    }
}