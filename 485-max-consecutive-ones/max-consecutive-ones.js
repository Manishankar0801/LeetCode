/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
  let currCount = 0
  let maxCount = 0

    for (let i =0;i<nums.length;i++) {
        if (nums[i] === 0) {
            maxCount = Math.max(maxCount, currCount)
            currCount = 0
        } else {
            currCount++
        }
    
    }
    return Math.max(maxCount, currCount) 
};

// If the current element is 0, we update maxCount and reset currCount
  // If the current element is 1, we increment currCount
  // At the end of the loop, we return the maximum of maxCount and currCount
  // This ensures we account for the case where the array ends with 1s
  // Time Complexity: O(n) where n is the length of the input array nums.
  // Space Complexity: O(1) since we are using only a few variables to keep