class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        pge = [0] * n
        nge = [0] * n

        max_ele = 0
        for i in range(n):
            max_ele = max(height[i] , max_ele)
            pge[i] = max_ele

        
        max_ele = 0

        for i in range(n-1,0,-1):
            max_ele = max(height[i] , max_ele)
            nge[i] = max_ele

        

        for i in range(len(nge)):
            nge[i] = min(nge[i],pge[i])

        water = 0
        for i in range(n):
            if nge[i] > height[i]:
                water += (nge[i] - height[i])

        return water

            

        