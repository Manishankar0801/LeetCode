class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, b in enumerate(nums):
            value = target - b
            if value in a:
                c = a[value]
                return [i, c]
            else:
                a[b] = i
        return []
        
        