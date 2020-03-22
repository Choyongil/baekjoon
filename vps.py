# 9012번 VPS문제


n = int(input())
result = []

for _ in range(n):
    arr = input()
    a, b, k = 0, 0, 0

    for i in range(len(arr)):
        if arr[i] == '(':
            a += 1
        elif arr[i] == ')':
            b += 1
        if b > a:
            k = 1
            break

    if a != b or k == 1:
        result.append('NO')
    else:
        result.append('YES')

for results in result:
    print(results)