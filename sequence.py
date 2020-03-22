# 15649번 수열

n, m = list(map(int, input().split()))

# arr = []
# for i in range(n):
#     arr.append(i + 1)
#
# check_list = [False] * n
# check = []
#
#
# def seqd(num):
#     # if num == m:
#     #     for j in range(m):
#     #         print(check[j], end= ' ')
#     #     print()
#     #     return
#
#     for k in range(n):
#         if check_list[k]:
#             continue
#
#         check_list[k] = True
#         check.append(arr[k])
#         seqd(num + 1)
#         check.pop()
#         check_list[k] = False
#
#
# seqd(0)



arr2 = [i+1 for i in range(n)]

check_list2 = [False] * n
check = []

def dfs(ctn):
    # if ctn == m:
    #     for i in range(m):
    #         print(check[i], end = ' ')
    #     print()
    #     return

    for k in range(n):
        if(check_list2[k]):
            continue

        check_list2[k] = True
        check.append(arr2[k])
        dfs(ctn+ 1)
        check.pop()
        check_list2[k] = False

dfs(0)




















