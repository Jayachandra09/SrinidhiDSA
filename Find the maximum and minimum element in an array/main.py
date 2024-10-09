#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        mini = float("inf")
        maxi = float("-inf")
        for i in range(len(arr)):
            if mini>arr[i]:
                mini = arr[i]
            if maxi<arr[i]:
                maxi = arr[i]
        return mini, maxi


# Link : https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
