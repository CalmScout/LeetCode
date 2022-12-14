// Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
// He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he
// will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more
// than the previous Monday. Given n, return the total amount of money he will have in the
// Leetcode bank at the end of the nth day.
impl Solution {
    pub fn total_money(n: i32) -> i32 {
        let k: i32 = n / 7;
        let p: i32 = n % 7;
        let mut result: i32 = 0;
        for a1 in 1..(k+1) {
            result += (2 * a1 + 7 - 1) * 7 / 2;
        }
        let a1: i32 = k + 1;
        result += (2 * a1 + p - 1) * p / 2;
        result
    }
}