class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            d=dict()
            
            for j in range(i+1,len(nums)):
                b = -(nums[i]+nums[j])
                if nums[j] in d:
                    a=[nums[i],nums[j],b]
                    a.sort()
                    if a not in result:
                        result.append(a)
                else:
                    d[b]=nums[j]
        return result
                    
       