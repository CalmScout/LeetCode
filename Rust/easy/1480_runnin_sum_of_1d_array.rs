// Given an array nums. We define a running sum of an array 
// as runningSum[i] = sum(nums[0]…nums[i]).
// Return the running sum of nums.
impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = Vec::new();
        let mut sum: i32 = 0;
        for i in 0..nums.len() {
            sum += nums[i];
            res.push(sum);
        }
        res
    }
}
