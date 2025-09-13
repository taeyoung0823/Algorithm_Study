def solution(nums):
    len_num = len(nums)
    nums=set(nums)
    return min(len(nums),len_num/2)