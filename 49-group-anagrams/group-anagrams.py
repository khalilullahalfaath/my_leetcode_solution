class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key_string stores unique word
        key_string = dict()
        for i in strs:
            # sort each item
            sorted_i = "".join(sorted(i))
            # check if sorted items exist 
            if sorted_i not in key_string :
                key_string[sorted_i] = []
        
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in key_string.keys():
                key_string[sorted_i].append(i)
        
        res = []
        for i in key_string:
            res.append(key_string[i])
        return res
            
