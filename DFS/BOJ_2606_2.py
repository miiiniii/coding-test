from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(r):
    q = deque([r])
    visited[r] = True
    cnt = 0

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                cnt += 1
    
    print(cnt)

bfs(1)
