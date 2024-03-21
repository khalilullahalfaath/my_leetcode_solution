class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = dict()
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 0
            else:
                nums_dict[i] += 1
        # print(list(nums_dict))
        sorted_nums = sorted(nums_dict.items(), key=lambda x:x[1], reverse=True)[0:k]
        # print(sorted_nums)
        return dict(sorted_nums).keys()