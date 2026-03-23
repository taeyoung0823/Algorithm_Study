from collections import deque

def solution(name):
    answer = 0
    name_list=list(name)
    n = len(name)
    
    for char in name:
        diff = ord(char)-ord('A')
        answer += min(diff, 26-diff)
        
    start_state = (['A'] * n)
    start_state[0] = name_list[0]
    
    queue = deque([(start_state, 0, 0)])
    visited = set()
    
    while queue:
        curr_name, curr_idx, move_count = queue.popleft()
        
        if curr_name==name_list:
            return answer + move_count
        
        state_key = ("".join(curr_name), curr_idx)
        if state_key in visited:
            continue
        visited.add(state_key)
    
        r_idx = (curr_idx + 1) % n
        r_name = curr_name[:]
        r_name[r_idx] = name_list[r_idx]
        queue.append((r_name, r_idx, move_count + 1))
    
        l_idx = (curr_idx - 1) % n
        l_name = curr_name[:]
        l_name[l_idx] = name_list[l_idx]
        queue.append((l_name, l_idx, move_count + 1))
    

    return answer