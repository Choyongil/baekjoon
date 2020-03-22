# 4949번 균형잡힌 문장

results = []

while True:
    strs = input()

    if strs == '.':
        break

    arr = []

    for i in strs:
        if i == '(' or i == '[':
            arr.append(i)

        if i == ')':
            if len(arr) == 0:
                break
            if arr[-1] == '(':
                arr.pop()
            else:
                break

        if i == ']':
            if len(arr) == 0:
                break
            if arr[-1] == '[':
                arr.pop()
            else:
                break

    if len(arr) == 0 and i == strs[-1]:
        results.append('yes')
    else:
        results.append('no')


for result in results:
    print(result)