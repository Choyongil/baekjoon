# 2389 설탕 분배 봉지 문제(3kg, 5kg)

a, b, result = 0, 0, 0

n = int(input())

while(n > 0):
    if n % 5 == 0:
        a = n / 5
        result = a+b
        break
    if n % 3 == 0:
        b = n / 3
        result = a+b

    n -= 5
    a += 1

if result == 0:
    print(-1)
else:
    print(int(result))