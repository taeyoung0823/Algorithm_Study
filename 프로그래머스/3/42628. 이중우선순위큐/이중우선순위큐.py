import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    alive = []
    uid = 0

    def clean_min():
        while min_heap and not alive[min_heap[0][1]]:
            heapq.heappop(min_heap)

    def clean_max():
        while max_heap and not alive[max_heap[0][1]]:
            heapq.heappop(max_heap)

    for op in operations:
        cmd, num = op.split()

        if cmd == "I":
            x = int(num)
            alive.append(True)
            heapq.heappush(min_heap, (x, uid))
            heapq.heappush(max_heap, (-x, uid))
            uid += 1

        else:  
            if num == "1":  
                clean_max()
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    alive[idx] = False
            else:           
                clean_min()
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    alive[idx] = False

    clean_min()
    clean_max()

    if not min_heap or not max_heap:
        return [0, 0]

    max_val = -max_heap[0][0]
    min_val = min_heap[0][0]
    return [max_val, min_val]
