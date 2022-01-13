class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = {}
        ans = []
        for i in nums1:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1
        for i in nums2:
            if i in check:
                check[i] -= 1
                if check[i] == 0:
                    del check[i]
                ans.append(i)
        return ans