def BS(A, X):
    l = 0
    r = len(A) - 1

    while l < r:
        mid = (l + r) // 2

        if A[mid] < X:
            l = mid + 1
        elif A[mid] > X:
            r = mid - 1
        else:
                res = mid
                l = mid+1

    return res

A = [1, 3, 5, 7, 7, 11, 11, 13, 15]
X = 7
result = BS(A, X)

if result != -1:
    print(f"Element {X} found at index {result}")
else:
    print(f"Element {X} not found in the array")
