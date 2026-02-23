from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    cmd = input().split()
    op = cmd[0]

    if op == "push_front":
        d.appendleft(cmd[1])
    
    elif op == "push_back":
        d.append(cmd[1])
    
    elif op == "pop_front":
        print(d.popleft() if d else -1)

    elif op == "pop_back":
        print(d.pop() if d else -1)
    
    elif op == "size":
        print(len(d))
    
    elif op == "empty":
        print(0 if d else 1)
    
    elif op == "front":
        print(d[0] if d else -1)

    elif op == "back":
        print(d[-1] if d else -1)