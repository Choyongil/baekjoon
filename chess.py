# 1018번 체스판 찾기

arr = []

a = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

b = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

n, m = map(int,input().split())

for _ in range(n):
    arr.append(input())

check = 64

for j in range(m-7):
    for i in range(n-7):
        min1 = 0
        min2 = 0

        for k in range(8):
            for l in range(8):
                if check < min1 and check < min2:
                    break
                if arr[k+i][l+j] != a[k][l]:
                    min1 += 1
                if arr[k + i][l + j] != b[k][l]:
                    min2 += 1

        if check > min1:
            check = min1
        if check > min2:
            check = min2

print(int(check))