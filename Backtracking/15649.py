n, m = map(int, input().split())
answer = []


def backtracking():

# 탈출 조건 세우기
    if len(answer) == m:
        # 출력하고 끝내기
        print(" ".join(map(str, answer)))    # 공백 한칸 문자열 형태로 붙여서 출력
        return

# 중복 숫자가 있는지 확인
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)    # 현재 선택 추가
            backtracking()      # 다음 단계 탐색
            answer.pop()

backtracking()


# 순열 라이브러리 사용, 메모리 동일 더 빠름
from itertools import permutations
n, m = map(int, input().split())

p = permutations(range(1, n+1), m)
for i in p:
    print(" ".join(map(str, i)))