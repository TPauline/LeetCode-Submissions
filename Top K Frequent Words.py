class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = {}
        words.sort()
        for i in words:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        print(h)
        
       
        h = sorted(h.items(), key = lambda i :i[1], reverse = True)
        print(h)
        j = 0
        words=[]
        for s,i in h:
            if j < k:
                j+=1
                words.append(s)
        return words
                
