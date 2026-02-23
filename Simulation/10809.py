# 등장하는 위치 
arr = [-1] * 26
s = input()

for word in s:
    arr[ord(word) - ord('a')] += 1

print(arr)