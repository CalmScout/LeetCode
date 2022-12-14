// Balanced strings are those who have equal quantity of 'L' and 'R' characters.
// Given a balanced string s split it in the maximum amount of balanced strings.
// Return the maximum amount of splitted balanced strings.
impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let mut x: i32 = 0;
        let mut split_count: i32 = 0;
        let s_bytes = s.as_bytes();
        for idx in 0..s.len() {
            if s_bytes[idx] as char == 'R' {
                x += 1;
            } else {
                x -= 1;
            }
            if x == 0 {
                split_count += 1;
            }
        }
        split_count
    }
}