class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #######################
        # brute force approach#
        #######################

        # key_dict = dict()
        # for i in range(len(nums)):
        #     key_dict[i] = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             key_dict[i] *= nums[j]
        # return key_dict.values()

        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        # print(n, left, right, result)

        # from left
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        # from right
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        # multiply to get the result
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result