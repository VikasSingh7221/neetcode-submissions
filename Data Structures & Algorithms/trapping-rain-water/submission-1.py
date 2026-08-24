class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        
        left_max = heights[l]
        right_max = heights[r]
        water = 0
        
        
        print(l,r,left_max,right_max)
        
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, heights[l])
                water += left_max - heights[l]
                
            else:
                r -= 1
                right_max = max(right_max, heights[r])
                water += right_max - heights[r]
                
        return water

            

        