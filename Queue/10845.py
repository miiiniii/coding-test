from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()
    op = cmd[0]

    if cmd[0] == "push":
        q.append(cmd[1])

    elif cmd[0] == "pop":
        print(q.popleft() if q else -1)
    
    elif cmd[0] == "size":
        print(len(q))
    
    elif cmd[0] == "empty":
        print(0 if q else 1)
    
    elif cmd[0] == "front":
        print(q[0] if q else -1)
    
    elif cmd[0] == "back":
        print(q[-1] if q else -1)
