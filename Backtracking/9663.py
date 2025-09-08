n = int(input())
answer = 0
raw = [0] * n # 왜 0으로 초기화하고, n개지?

# 행번호 x번 부터 검사 시작
def is_promising(x):
    for i in range (x):
        if raw[x] == raw[i] or abs(raw[x] - raw[i]) == abs(x - i):
            return False

    return True

def n_queens(x):
    global answer

    # 탈출 조건 만들기
    if x == n:
        answer += 1
        return

    else:
        for i in range(n):
            raw[x] = i  # [x, i]에 퀸 놓기
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(answer)