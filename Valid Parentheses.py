class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s == "":
            return False
    
        for i in s:
            if i == "(" or i =="[" or i == "{":
                stack.append(i)
            else:
                
                print("...")
                if stack:
                    t = stack.pop(-1)
                    print(i,t)
                    if t == "(" and  i !=")":
                        print(",,,")
                        return False
                    elif t == "{" and not i =="}":
                        return False
                    elif t == "[" and not i =="]":
                        return False
                else:
                    return False
        if len(s) == len(stack) or stack:
            return False
        return True
