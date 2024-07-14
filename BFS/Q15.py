# 특정 거리의 도시 찾기 https://www.acmicpc.net/problem/18352
# 난이도 1.5, 풀이 시간 30분, 시간 제한 2초, 메모리 제한 256MB

""" 문제:
어떤 나라에는 1~N번까지의 도시와 M개의 단방향 도로가 존재합니다.
모든 도로의 거리는 1이고, 특정한 도시 X로부터 출발해 도달할 수 있는 모든 도시 중에서
최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램 작성하세요.
(출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정)

모든 간선의 비용 동일 => BFS
"""

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[]for _ in range (n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)