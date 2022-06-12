def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, n
    current_idx = -1
    while(left <= right):
        mid = (left + right) // 2
        if mid * mid <= n:
            left = mid + 1
            current_idx = mid
        else:
            right = mid -1
    return current_idx

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
