def solution(word):
    vowels = ['A','E','I','O','U']
    words = []
    
    def dfs(cur):
        if cur:
            words.append(cur)
        if len(cur)==5:
            return
        for v in vowels:
            dfs(cur+v)
    
    dfs("")
    
    return words.index(word)+1