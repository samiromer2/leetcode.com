class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        # left pass
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # right pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer