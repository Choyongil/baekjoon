# 15650번 수열 2번째

n, m = list(map(int, input().split()))

arr = [i for i in range(1,n+1)]
check = []

def seq(ctn, array, l):
    if sorted(check) in array:
        return
    # if ctn == m:
    #     # l+=1
    #     # print('ctn :',ctn,' check :',sorted(check))
    #     array.append(sorted(check))
    #     for k in range(m):
    #         print(check[k], end = ' ')
    #     print()
    #     return

    for i in range(n):
        l += 1
        check.append(arr[i])
        seq(ctn+1, array, l)
        check.pop()
    print('l :',l,' i :',i)


seq(0,[], 1)