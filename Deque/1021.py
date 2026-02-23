"""
원하는 인덱스를 뽑는데 필요한 최소 회전 수를 구하기
단, 회전은 왼쪽 or 오른쪽 둘 중 횟수가 적은 방향으로
"""

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = deque(range(1, n+1))
targets = list(map(int, input().split()))  # 둘째줄의 m개의 숫자를 담는 리스트
count = 0

for t in targets:
    idx = d.index(t)  # 덱의 원소는 1부터 n이고, 입력받은 숫자 t보다 1 작아서
    
    # 왼쪽으로 회전
    if idx <= len(d)//2:
        for _ in range(idx):
            d.append(d.popleft())
            count += 1
    # 오른쪽으로 회전
    else:
        for _ in range(len(d) - idx):
            d.appendleft(d.pop())
            count += 1
    
    # 원소가 가장 앞에 왔으면 제거하기
    d.popleft()

print(count)