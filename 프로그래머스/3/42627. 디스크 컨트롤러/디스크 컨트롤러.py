import heapq

def solution(jobs):
    heapq.heapify(jobs)
    ready = []
    total = 0
    t = 0
    done = 0
    n = len(jobs)
    
    while done < n:
        while jobs and jobs[0][0] <= t:
            req, dur = heapq.heappop(jobs)
            heapq.heappush(ready, (dur, req))

        if not ready:
            t = jobs[0][0]
            continue

        dur, req = heapq.heappop(ready)
        t += dur
        total += (t - req)
        done += 1

    return total // n
