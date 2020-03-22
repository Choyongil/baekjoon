# 10773번 제로 쓰면 최근 수 지우기

n = int(input())
arr = []

while(n > 0):
    n -= 1
    k = int(input())
    if k != 0:
        arr.append(k)
    else:
        if len(arr) != 0:
            del arr[-1]

print(sum(arr))
