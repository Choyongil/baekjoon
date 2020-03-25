# 1874번 스택을 이용한 수열
# 답은 나오는데 '출력초과'가 뜨는 경우

n = int(input())
seq = []
results = []
i = 1

while n > 0:
    n -= 1
    input_max = int(input())

    if len(seq) == 0:
        seq.append(i)
        results.append('+')
        i += 1

    while seq[len(seq) - 1] < input_max:
        seq.append(i)
        results.append('+')
        i += 1

    if seq[len(seq) - 1] == input_max:
        seq.pop()
        results.append('-')
    else:
        results = []
        results.append('NO')
        break

for result in results:
    print(result)
