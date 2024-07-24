# selection sort
def selection(A):
  for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
      if A[min_idx] > A[j]:
        min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
  return A

A = [12, 11, 13, 5, 6]
print(selection(A))
