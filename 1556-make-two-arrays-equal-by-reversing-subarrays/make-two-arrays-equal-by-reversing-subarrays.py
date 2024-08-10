class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # return True if the arr only contains 1 element
        if len(arr) == 1 and arr[0] == target[0]:
            return True

        # arr = 2 4 1 3
        # target = 1 2 3 4 
        # arr -> find the first elemen equals to first element
        # then reverse it
        # arr -> 1 4 2 3
        # 

        for i in range(len(target)):
            if arr[i] == target[i]:
                continue
            
            j = i
            while j < len(arr) and arr[j] != target[i]:
                j += 1
            

            if j == len(arr):
                return False

            # reverse
            arr[i:j+1] = arr[i:j+1][::-1]
 
        return arr == target


        
