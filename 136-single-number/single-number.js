/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let hash = {}
    for (const value of nums) {
        if (hash[value]) {
            hash[value]++
        } else {
            hash[value] = 1
        }
    }
    console.log(hash)
    for (const value of nums) {
        if (hash[value] === 1) {
            return value
        }
    }
};