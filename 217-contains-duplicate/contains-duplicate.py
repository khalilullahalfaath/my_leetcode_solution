class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set approach
        number_unique = set()
        for i in nums:
            if i in number_unique:
                return True
            number_unique.add(i)
        return False
        