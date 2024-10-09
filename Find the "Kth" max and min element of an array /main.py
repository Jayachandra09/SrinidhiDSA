#User function Template for python3


class Solution:
    
    # def MergeProcedure(self, arr, i, mid, j):
    #     m = mid-i+1
    #     n = j-(mid+1)+1
        
    #     left = [0]*m
    #     right = [0]*n
        
    #     for indx in range(m):
    #         left[indx] = arr[i+indx]
    #     for indx in range(n):
    #         right[indx] = arr[(mid+1)+indx]
            
    #     p = 0
    #     q = 0
    #     k = i
    #     while p<len(left) and q<len(right):
    #         if left[p]<right[q]:
    #             arr[k]=left[p]
    #             p+=1
    #         else:
    #             arr[k]=right[q]
    #             q+=1
    #         k+=1
    #     while p<len(left):
    #         arr[k]=left[p]
    #         p+=1
    #         k+=1
    #     while q<len(right):
    #         arr[k]=right[q]
    #         q+=1
    #         k+=1
    
    # def MergeSort(self, arr, i, j):
    #     mid = i+(j-i)//2
    #     if i<j:
    #         self.MergeSort(arr, i , mid)
    #         self.MergeSort(arr, mid+1, j)
            
    #         self.MergeProcedure(arr, i, mid, j)

    # def kthSmallest(self, arr,k):
    #     i = 0
    #     j = len(arr)-1
    #     self.MergeSort(arr, i, j)
    #     if k<=len(arr):
    #         return arr[k-1]
    #     return None
    def kthSmallest(self, arr,k):
        max_element = max(arr)

    # Create a dictionary to store the frequency of each 
    # element in the input array
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

    # Keep track of the cumulative frequency of elements 
    # in the input array
        count = 0
        for i in range(max_element + 1):
            if i in freq:
                count += freq[i]
                if count >= k:
                # If we have seen k or more elements, 
                # return the current element
                    return i

        return -1

  #Link : https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
  #I solved using merge Sort,Need to revise Heapq and Quick selection sort to meet the required time complexity
