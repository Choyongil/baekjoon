# 1874번 스택을 이용한 수열
# 답은 나오는데 왜 '출력초과'가 뜨는 경우

n = int(input())

seq = [int(input()) for _ in range(n)]
seq.reverse()

checks = []
results = []

j = 1

m = seq.index(max(seq))
check = []

for i in range(m):
    check.append(seq[i])

if sorted(check) == check:
    while len(seq) != 0 and j != n+1:

        checks.append(j)
        results.append('+')

        while seq[-1] == checks[-1] and len(seq) != 0:
            seq.pop()
            checks.pop()
            results.append('-')
            if len(checks) == 0:
                break
        j += 1

    for result in results:
        print(result)

else:
    print('NO')
