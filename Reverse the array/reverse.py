class Solution:
    def reverseArray(self, arr):
        # code here
        mid = len(arr)//2
        n = len(arr)
        for i in range(mid):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        
      if __name__=="main":
            reverseArray(arr)
            for i in range(n):
                print(arr[i], end=" ")
            
            
        
        
