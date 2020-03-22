# 2798 블랙잭

arr = []
max_list = []

n, maximum = map(int, input().split())
op = list(map(int, input().split()))

for i in range(n):
    arr.append(op[i])

arr.sort()
for i in range(n):
    max_list.append(arr[i])
    for j in range(n - 1 - i):
        for r in range(n - 2 - i - j):
            result = arr[i]
            if maximum >= (result + arr[j + 1 + i] + arr[r + 2 + i + j]):
                result = result + arr[j + 1 + i] + arr[r + 2 + i + j]

                if max_list[i] < result:
                    max_list[i] = result

print(max(max_list))