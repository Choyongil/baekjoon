# 2409 긴 파이프로 짧은 파이프를 최대 갯수로 만들기


M = int(input())    # 긴 파이프 갯수

long_pipe = list(map(int, input().split()))     # 긴 파이프들의 길이

N = int(input())    # 짧은 파이프 갯수

short_pipe = list(map(int, input().split()))    # 짧은 파이프들의 길이

long_pipe.sort(reverse = True)

max = 0
while M > 0:
    for i in len(long_pipe):
        for j in len(short_pipe):
            if (long_pipe[i] - short_pipe[j]) > 0:
                long_pipe[i] -= short_pipe[j]
