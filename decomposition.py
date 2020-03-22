# 2231번 분해합

num = int(input())
result = 0

for n in range(1, num+1):

    sum2 = list(map(int,str(n)))
    result = n + sum(sum2)

    if num == result:
        print(n)
        break

    if n == num:
        print(0)
