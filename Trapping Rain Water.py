class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft =[0]
        maxright =[0]
        water= 0
#         for i in range(1,len(height)):
#             maxleft.append(max(height[:i]))
#             maxright.append(max(height[-i:]))
#         maxright = maxright[::-1]
#         print(maxleft)
#         print(maxright)
        

#         for i in range(len(height)):
#             water += min(maxleft[i],maxright[i])-height[i] if min(maxleft[i],maxright[i])-height[i] > 0 else 0

#         l = 0
#         r = len(height)-1
#         i = 0
#         maxl = 0
#         maxr = 0
#         while i < len(height) :
#             if l<i or r >i:
#                 if l < i:
#                     maxl = max(height[l], maxl)
#                     l+=1

#                 if r > i:
#                     maxr = max(height[r], maxr)
#                     r-=1
#             else:
#                 water += (min(maxl, maxr)- height[i]) if (min(maxl, maxr) - height[i]) > 0 else 0
#                 l = 0
#                 r = len(height)-1
#                 maxl = 0
#                 maxr = 0
#                 i+=1 
#         return water

        l = 0
        r = len(height)-1
        i = 0
        maxl = 0
        maxr = 0
        for i in range(1,len(height)-1):
            maxl = max(height[:i]) if max(height[:i]) else 0
            maxr = max(height[i+1:]) if max(height[i+1:]) else 0
            water += (min(maxl, maxr)- height[i]) if (min(maxl, maxr) - height[i]) > 0 else 0
            
        return water
