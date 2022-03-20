class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        

    def addNum(self, val: int) -> None:
        newpair = [val,val]
        temp = []
        for i in range(len(self.lst)):
            curr = self.lst[i]
            if curr[0]-1 > newpair[1]: # newpair at end < curr start -1
                temp.append(newpair)
                newpair=curr
            elif curr[1]+1 < newpair[0]:
                temp.append(curr)
            else:
                newpair = [min(curr[0],newpair[0]),max(curr[1],newpair[1])]
        temp.append(newpair)
        self.lst = temp

    def getIntervals(self) -> List[List[int]]:
        return self.lst
        
