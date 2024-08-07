# https://www.acmicpc.net/problem/2606
# 시간 제한 1초, 메모리 제한 128MB

""" 문제:
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스가 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

첫째 줄에는 컴퓨터의 수가 주어진다. 
컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

=> 해당 컴퓨터와 연결된 컴퓨터의 개수를 모두 구하면 됨.(DFS/BFS 모두 가능)
"""

# 컴퓨터의 개수(노드)
n = int(input())

# 컴퓨터끼리 연결된 선의 개수(엣지)
m = int(input())

# 노드 번호가 1부터 시작하기 때문에 n+1
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 주의! 연결된 컴퓨터 정보가 1부터 등장한다는 보장 x
    # 5번 노드부터 줄 수 있기때문에 graph[a] 와 graph[b] 동시에 연결 정보를 저장
    graph[a].append(b)
    graph[b].append(a)

# 재귀적 구현
def dfs(x):
    global count
    visited[x] = True
    count += 1
    for node in graph[x]:
        if visited[node]:
            continue
        dfs(node)

# 연결된 컴퓨터 수 저장하는 변수
count = 0
visited = [False for _ in range(n+1)]

# 노드 1부터 DFS 실행
dfs(1)
print(count-1)