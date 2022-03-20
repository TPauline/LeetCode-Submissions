class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for i in range(len(intervals)): 
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        start.sort()
        end.sort()
        count = 0
        s=0
        e = 0
        res =0
        while s < len(start) and e < len(end):
            if start[s]< end[e]:
                count+=1
                s+=1
            elif end[e]<=start[s]:
                count-=1
                e+=1
            res = max(res,count)
        return res
