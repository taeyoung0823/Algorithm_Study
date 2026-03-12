import itertools

def solution(numbers):
    num=0
    arr = list(numbers)
    nums = []

    for i in range(1, len(numbers) + 1):
        for p in itertools.permutations(arr, i):
            nums.append(int(''.join(p)))

    nums = set(nums)
    
    for i in nums:
        now = True
        for j in range(2,int(i**(1/2))+1):
            if i%j==0:
                now = False
        if now == True and i !=0 and i != 1:
            num+=1
        
    return num