class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,n in enumerate(nums):
            value = target - n
            if value in result:
                return [i, result[value]]
            result[n] = i
        