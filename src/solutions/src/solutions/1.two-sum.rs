/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 */

// @lc code=start
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for (i, &num) in nums.iter().enumerate() {
            for (j, &num2) in nums.iter().enumerate() {
                if i != j && num + num2 == target {
                    return vec![i as i32, j as i32];
                }
            }
        }
        vec![-1, -1]
    }
}
// @lc code=end

