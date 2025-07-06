/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let x = 0
    for (const value of nums) {
        x = x ^ value
    }
    return x
};