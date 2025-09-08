L, C = map(int, input().split())
answer = []
arr = input().split(" ") 
arr.sort()   

def backtracking(index, level):
    if len(answer) == L:
        print(" ".join(answer))
        return
    for i in range(index, level):
        answer.append(arr[i])
        backtracking(index+1, level+1)
        answer.pop()

backtracking('a', 0)