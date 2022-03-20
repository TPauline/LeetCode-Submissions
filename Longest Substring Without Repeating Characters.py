class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
 
        maxs =[]
        for i in range(len(s)): #go thorugh each element
            l = []
            for j in range(i,len(s)): # from current I 
                if s[j] not in l:
                    l.append(s[j])
                else:
                    break
            #print(l)
            maxs.append(len(l))
        return max(maxs)
   

                
        
        
