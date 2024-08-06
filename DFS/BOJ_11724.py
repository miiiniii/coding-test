# https://www.acmicpc.net/problem/11724
# 시간 제한 3초, 메모리 제한 512MB

"""문제:
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

<IN> 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
    (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
    (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

<OUT> 첫째 줄에 연결 요소의 개수를 출력한다.
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 정점의 개수, 간선의 개수
n, m = map(int, input().split()) 

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


count = 0 # 연결 노드의 수
visited = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1 # dfs 한 번 끝날 때마다 count+1

print(count)
 