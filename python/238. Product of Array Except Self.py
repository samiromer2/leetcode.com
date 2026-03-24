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
    

#     class Solution:
#     def productExceptSelf(self, nums):
#         n = len(nums)
        
#         left = [1] * n
#         right = [1] * n
#         answer = [1] * n
# # [2,3,4]
# #n = 3
#         # build left array
#         for i in range(1, n):
#             left[i] = left[i - 1] * nums[i - 1]
           

#         # build right array
#         for i in range(n - 2, -1, -1):
#             right[i] = right[i + 1] * nums[i + 1]
           

#         # combine
#         for i in range(n):
#             answer[i] = left[i] * right[i]

#         return answer