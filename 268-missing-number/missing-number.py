class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        for num in nums:
            expected_sum -= num
        return expected_sum
        