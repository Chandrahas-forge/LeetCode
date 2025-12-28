class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        used = []
        # heapq.heapify(available)
        print(available)
        ans = [0]*n
        meetings.sort()
        time = meetings[0][0]
        for cms, cme in meetings:

            while(used and used[0][0]<=cms):
                end_time, room_no = heapq.heappop(used)
                heapq.heappush(available, room_no)
            
            if not available:
                end_time, room_no = heapq.heappop(used)
                ans[room_no]+=1
                heapq.heappush(used,(end_time+(cme-cms),room_no))
            else:
                room_no = heapq.heappop(available)
                ans[room_no]+=1
                heapq.heappush(used,(cme,room_no))
        print(ans)
        max_v = max(ans)
        for i,v in enumerate(ans):
            if v==max_v:
                return i
        return 0
        
