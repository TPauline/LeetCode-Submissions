class Solution:
    def frequencySort(self, s: str) -> str:
        print(ord("a"),ord("A"),ord("b"))
        s = sorted(s)
        r =[]
        j=s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                j+=s[i]
            else:
                r.append(j)
                j=s[i]
        r.append(j)
        r.sort(key=lambda i : len(i), reverse = True )
        print("".join(r))
        return "".join(r)
