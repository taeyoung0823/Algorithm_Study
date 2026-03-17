def dfs(x,graph,visited):
    visited[x] = True
    count = 1
    
    for next_node in graph[x]:
        if not visited[next_node]:
            count+=dfs(next_node,graph,visited)
    return count

def solution(n, wires):
    answer = n
    wir = len(wires)
    
    for i in range(wir):
        graph = [[] for _ in range(n+1)]
        for j in range(wir):
            if i==j:
                continue
            a,b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
    
        visited = [False]*(n+1)
        k = dfs(1,graph,visited)
        diff = abs(k-(n-k))
        answer = min(answer,diff)
    
    return answer