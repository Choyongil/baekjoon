# 1920번 수 찾기

# 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1≤M≤100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

def binarysearch(low, high, check, arr):

    if low > high:
        return False

    mid = (low + high) // 2

    if arr[mid] > check:
        return binarysearch(low, mid - 1, check, arr)
    elif arr[mid] < check:
        return binarysearch(mid + 1, high, check, arr)
    else:
        return True


n = int(input())
find_arr = sorted(list(map(int, input().split())))

m = int(input())
check_arr = list(map(int, input().split()))

results = []

for check in check_arr:

    if binarysearch(0, n-1, check, find_arr):
        results.append(1)
    else:
        results.append(0)

for result in results:
    print(result)