// Given a square matrix mat, return the sum of the matrix diagonals.
// Only include the sum of all the elements on the primary diagonal and
// all the elements on the secondary diagonal that are not part of the
// primary diagonal.


impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let mut res: i32 = 0;
        for i in 0..mat.len(){
            res += mat[i][i] + mat[i][mat.len() -1 - i];
        }
        if mat.len() % 2 == 1 {
            res -= mat[mat.len() / 2][mat.len() / 2];
        }
        res
    }
}