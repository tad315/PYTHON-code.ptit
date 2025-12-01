import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

def merge_count(arr, l, r):
    if l >= r:
        return 0
    
    mid = (l + r) // 2
    cnt = merge_count(arr, l, mid) + merge_count(arr, mid + 1, r)
    
    temp = []
    i, j = l, mid + 1
    
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            cnt += (mid - i + 1)
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1

    arr[l:r+1] = temp
    return cnt


n = int(input())
arr = list(map(int, input().split()))
print(merge_count(arr, 0, n - 1))
