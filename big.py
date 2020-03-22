#7568번 덩치 순위 메기기

num = int(input())
arr = []
arr2 = []
for i in range(num):
    arr.append(list(map(int, input().split())))
    arr2.append(1)

for i in range(num):
    for j in range(num):
        if i == j:
            continue
        elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            arr2[i] += 1
# for i in range(num):
#     # print(arr2[i], end=' ')
# print()
