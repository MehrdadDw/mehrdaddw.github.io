def maxArea(height) -> int:
        res=0

        length=len(height)
        for x in range(length):
            if height[x]==0:
                continue
            prev_y=0
            for y in range(length-1,x,-1):
                if (height[y]<=prev_y):
                    
                    continue
                prev_y=height[y]
        
                area=min(height[x],height[y])*(y-x)

                if (res<area):
                    res=area
        return res
print(maxArea([2,3,4,5,18,17,6]))