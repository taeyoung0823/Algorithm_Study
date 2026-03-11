from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    now = 0
    
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    while truck_weights or now > 0:
        time += 1
        
        out = bridge.popleft()
        now -= out
        
        if truck_weights and now + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            now += truck
        else:
            bridge.append(0)
    
    return time