//Given an array of numbers arr. A sequence of numbers is 
//called an arithmetic progression if the difference between
//any two consecutive elements is the same.
//Return true if the array can be rearranged to form an arithmetic
//progression, otherwise, return false.
impl Solution {
    pub fn can_make_arithmetic_progression(arr: Vec<i32>) -> bool {
        let mut arr_copy = arr.clone();
        arr_copy.sort();
        let mut dx: i32 = arr_copy[1] - arr_copy[0];
        for idx in 2..arr_copy.len() {
            if arr_copy[idx] - arr_copy[idx - 1] != dx {
                return false
            }
        }
        true
    }
}