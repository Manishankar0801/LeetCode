class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result,n=0,len(arr)
        for i in range(len(arr)):
            end = i+1
            start = n-i
            total = start*end
            odd = total//2
            if total%2==1:
                odd+=1
            result+=odd*arr[i]
        return result