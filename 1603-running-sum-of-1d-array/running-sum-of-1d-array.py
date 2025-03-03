class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = 0
        for i, num in enumerate(nums):
            currSum = currSum + nums[i]
            nums[i] = currSum
        return nums

        