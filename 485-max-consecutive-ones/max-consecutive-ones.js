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