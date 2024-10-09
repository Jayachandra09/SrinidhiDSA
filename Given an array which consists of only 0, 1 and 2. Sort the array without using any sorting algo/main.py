class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        low = 0
        mid = 0
        high = len(arr)-1
        while mid<=high:
            if arr[mid]==0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[high], arr[mid] = arr[mid], arr[high]
                high-=1
        return arr

#Link : https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
