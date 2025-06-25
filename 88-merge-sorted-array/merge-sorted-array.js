/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let p1 = m - 1; // Pointer for the last element in nums1
  let p2 = n - 1; // Pointer for the last element in nums2

  for (let i = m + n - 1; i >= 0; i--) {
    if (p2 < 0) {
      break; // If p2 is out of bounds, we are done we can break the loop
    }
    // but if p1 breaks the condition then we can take nums2[p2] and put it in nums1[i]
    // p1 >= 0 ensures we don't go out of bounds of nums1
    // else it will go to else
    if (p1>=0 && nums1[p1] > nums2[p2]) {
      nums1[i] = nums1[p1];
      p1--;
    } else {
      nums1[i] = nums2[p2];
      p2--;
    }
  }
};