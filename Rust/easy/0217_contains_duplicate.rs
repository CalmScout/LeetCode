// Given an integer array nums, return true if any value appears at least twice in the array,
// and return false if every element is distinct.
use std::collections::HashSet;
use std::iter::FromIterator;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let set: HashSet<i32> = HashSet::from_iter(nums.iter().cloned());
        if set.len() < nums.len(){
            return true;
        } else {
            return false;
        }
    }
}