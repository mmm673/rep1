#A = list(map(str, input().split()))

A = [i+1 for i in range(30)]
for i in range(0, len(A), 3):
  A[i] = 'fizz'
for i in range(0, len(A), 5):
  if A[i] != 'fizz':
    A[i] = 'buzz'
  else:
    A[i] = 'fizzbuzz'

print(' '.join(map(str, A)))
