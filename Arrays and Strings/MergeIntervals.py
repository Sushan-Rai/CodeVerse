class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # for i in range(len(intervals)-1):
        #     for j in range(len(intervals)-i-1):
        #         if(intervals[j][0]>intervals[j+1][0]):
        #             intervals[j],intervals[j+1] = intervals[j+1],intervals[j]
        intervals.sort(key = lambda x:x[0])
        i=0
        # print(intervals)
        while i < len(intervals) - 1:
            if(intervals[i][1]>=intervals[i+1][0]):
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                # intervals[i][0] = min(intervals[i][0],intervals[i+1][0])
                intervals.pop(i+1)
            else:
                i+=1
        return intervals