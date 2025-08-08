from collections import deque
# ****** input() 사용하면 시간 초과
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [0] * (n+1)    # 노드
graph = [[]for _ in range(n+1)]


# 인접리스트
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

def bfs(r):
    q = deque()
    q.append(r)   # q = deque([r])
    visited[r] = 1
    cnt = 1
    
    while q:
        cur = q.popleft()   # cur = 방문처리 된 노드
        graph[cur].sort(reverse=True)   # 하나밖에 없지 않나

        for next in graph[cur]: # next = 방문처리 된 노드와 연결된 노드
            if not visited[next]:
                q.append(next)
                cnt+=1
                visited[next] = cnt

bfs(r)
for i in visited[1:]:
    print(i)
