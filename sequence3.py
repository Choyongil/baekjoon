# 15651번 수열3

n, m = list(map(int, input().split()))

arr = [ i for i in range(1,(n+1))]
check = []
check_list = [False] * n

def seq(ctn):

    # if ctn == m:
    #     for i in range(m):
    #         print(check[i], end = ' ')
    #     print()
    #     return

    for k in range(n):

        check.append(arr[k])
        seq(ctn+1)
        check.pop()

seq(0)
