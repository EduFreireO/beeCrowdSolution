def solution(a):
    maxSub = abs(a[1] - a[0])
    for index in range(2, len(a)):
        if abs(a[index] - a[index - 1]) > maxSub:
            maxSub = abs(a[index] - a[index - 1])
    return maxSub

