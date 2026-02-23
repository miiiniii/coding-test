"""
1번이 제일 위 -> 스택으로 생각하기 쉽지만, 1부터 n까지 쌓이므로 큐 쓰기
"""

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque(range(1, n+1))


while(len(q)!=1):
    q.popleft()    
    q.append(q.popleft())

print(q[0])