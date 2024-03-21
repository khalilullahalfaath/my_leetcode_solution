class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting the ASCII
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        return sorted_s == sorted_t
        