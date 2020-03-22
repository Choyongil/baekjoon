# 4344 케이스마다 평균보다 높은 학생 비율

import numpy as np

n = int(input())    # 케이스 수
result = []         # 케이스마다 평균 이상 비율 저장하는 배열

for _ in range(n):
    k = 0           # 평균보다 높은 학생 수
    arr = []
    op = list(map(int,input().split()))

    for i in range(op[0]):
        arr.append(op[i+1])

    mean = np.mean(arr)

    for j in range(op[0]):
        if op[j+1] > mean:
            k += 1

    a = float(k/op[0] * 100)
    result.append('%.3f' % a)

for j in range(len(result)):
    print(result[j] + '%')