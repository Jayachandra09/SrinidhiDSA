class Solution:
    def rotate(self, arr):
        temp = arr[-1]
        l = len(arr)-1
        while l>0:
            arr[l] = arr[l-1]
            l-=1
        arr[l]=temp
        return arr

# Input: arr = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
# Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.

#Link : https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1
