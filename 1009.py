
arr = []

n = input()
n = int(n)

for i in range(n):
    arr.append(input())

for i in range(n):
    a, b = arr[i].split()
    a = int(a)
    b = int(b)

    if a == 1:
        print(1)
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif b == 1:
        print(a)

    else:
        brr = []
        a2 = 1
        for j in range(b-1):
            a2 = (a * a2) % 10
            if a2 in brr:
                length = len(brr)
                print(brr[(b % length) - 1])
                break
            brr.append(a2)
        if( b <= len(brr)+1):
            print(brr[len(brr)-1]*a % 10)