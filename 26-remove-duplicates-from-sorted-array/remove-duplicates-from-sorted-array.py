class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer approach
        left = 1 # second element: not 0 because every first element is unique

        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
        return left