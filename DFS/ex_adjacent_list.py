# 인접 리스트
"""
구현: 파이썬 리스트
장점: 모든 노드를 순회할 때 편리
단점: 원하는 노드만 선택해서 확인할 수 없음, 앞에서부터 차례대로 확인해야함
=> edge 적은 희소 그래프일 때 인접 리스트 선택
"""

graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)