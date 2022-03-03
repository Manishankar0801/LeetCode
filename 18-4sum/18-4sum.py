class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = nums
        arr.sort()
        quadruplets = []
        for i in range(len(arr)-3):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1, len(arr)-2):
                if j > i + 1 and arr[j] == arr[j-1]:
                    continue
                left, right = j + 1, len(arr)-1
                while left < right:
                    quad_sum = arr[i] + arr[j] + arr[left] + arr[right] 
                    if quad_sum == target:
                        quadruplets.append([arr[i] , arr[j], arr[left], arr[right]])
                        left += 1 
                        right -=1
                        # avoid duplicates
                        while left < right and arr[left] == arr[left-1]:
                            left +=1  
                        while left < right and arr[right] == arr[right+1]:
                            right -= 1 
                        
                    elif quad_sum < target:
                        left += 1 
                    else: 
                        right -= 1
            
        return quadruplets