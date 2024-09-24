def max_subarray(arr):
    max_sum = float('-inf')
    sum = 0 
    n = len(arr)

    for i in range(n):
        for j in range(n):
            for k in range(i, j + 1):
                sum = sum + arr[k]
            max_sum = max(sum, max_sum)
            sum = 0

    return max_sum

def dyn_max_subarray(arr):
    n = len(arr)
    sums = [[0] * n for _ in range(n)]
    max_sum = float('-inf')

    for i in range(n):
        for j in range(i, n):
            if i == j:
                sums[i][j] = arr[i]
            else:
                sums[i][j] = sums[i][j - 1] + arr[j]
            max_sum = max(sums[i][j], max_sum)
    
    return max_sum 

def div_max_subarray(arr, start, end):
    if start > end:
        return float('-inf')
    
    if start == end:
        return arr[start]

    mid = (start + end) // 2
    left_max = div_max_subarray(arr, start, mid)    
    right_max = div_max_subarray(arr, mid + 1, end)

    left_side_sum = float('-inf')
    right_side_sum = float('-inf')

    temp_sum = 0
    for i in range(mid, start - 1, -1):
        temp_sum += arr[i]
        left_side_sum = max(left_side_sum, temp_sum)

    temp_sum = 0
    for i in range(mid + 1, end + 1):
        temp_sum += arr[i]
        right_side_sum = max(right_side_sum, temp_sum)

    mid_max = left_side_sum + right_side_sum    

    max_sum = max(left_max, mid_max, right_max)
    return max_sum


def main():
    arr = [-2 , -4, 3, -1, 5, 6, -7, -2, 4, -3, 2]
    print(max_subarray(arr))
    print(dyn_max_subarray(arr))
    print(div_max_subarray(arr, 0, len(arr) - 1))


if __name__ == '__main__':
    main()