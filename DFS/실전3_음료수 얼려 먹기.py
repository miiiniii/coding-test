# p.149 실전 문제 3.음료수 얼려 먹기
# 난이도 1.5, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB

""" 문제:
N x M 크기의 얼음틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.

"""
# N, M을 공백으로 구분해 입력받아햠
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):

    # 주어진 범위 벗어나면 종료
    if x <=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    # 현재 노드를 아직 방문 안했으면
    if graph[x][y] == 0:
        
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상, 하, 좌, 우 모두 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True
    return False

result = 0
# 입력받은 실제 N, M 적용
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            # 최종적으로 덩어리진 True의 개수 계산
            result += 1

print(result)