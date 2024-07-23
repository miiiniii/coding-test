def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')   # end=' ' 공백 문자를 사용해, 개행 없이 출력
    
    # 재귀적으로 현재 노드와 연결된 다른 노드 방문
    for i in graph[v]:
        if not visited[i]:
                dfs(graph, i, visited)


graph = [
    [], # 0번 노드에 연결된 노드 
    [2, 3, 8],  # 1번 노드에 연결된 노드
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]  # 8번 노드에 연결된 노드
]

visited = [False] * 9   # 노드의 방문 정보 담을 리스트. 노드0 ~ 노드8까지 총 9개 (단, 이 예시에서 노드 0은 없음)

dfs(graph, 1, visited)