class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0
        for account in accounts:
            currSum = sum(account)
            maxSum = max(maxSum, currSum)
        return maxSum