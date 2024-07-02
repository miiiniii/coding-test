# edge의 비용으로 연결 관계 표현
# INF -> 연결 X
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
