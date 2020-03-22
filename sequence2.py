# 15650번 수열 2번째

n, m = list(map(int, input().split()))

arr = [i for i in range(1,n+1)]
check = []
check_list = [False]*n

def seq(ctn, array):

    if ctn == m:
        if sorted(check) not in array:
            array.append(sorted(check))
            # for k in range(m):
            #     print(check[k], end = ' ')
            # print()
            # return
        else:
            return

    for i in range(n):
        if check_list[i]:
            continue

        check_list[i] = True
        check.append(arr[i])
        seq(ctn+1, array)
        check.pop()
        check_list[i] = False

seq(0,[])