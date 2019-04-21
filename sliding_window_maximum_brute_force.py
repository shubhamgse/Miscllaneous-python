class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        
        i = 0
        maxSpit = []
        output = []
        
        for i in range(len(nums)-k+1):
            
            for j in range(i, i+k+1):
                
                if(len(maxSpit) < k):
                    maxSpit.append(nums[j])
            
                else:
                    output.append(max(maxSpit))
                    maxSpit.clear()
          
            
        return output