from collections import deque

def solution(priorities, location):
    dq = deque(priorities)
    a = []
    while dq:
        cur = dq.popleft()
        if cur == max(dq):
            a.append(cur)
        else:
            dq.append(cur)
            
    print(a)

solution([2,1,3,2],2)
