import sys
input = sys.stdin.readline

stack = []

k= int(input())
for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))

""" 알고리즘
1. 정수 k 입력 받고 k만큼 입력받기
2. 스택(리스트) 생성
3-0. 0 들어오면 pop
3-1. 나머지는 append
4. 입력 다 받으면 sum 출력

"""