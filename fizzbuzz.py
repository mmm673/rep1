def replace(A):
  for i in range(len(A)):
    t = A[i]
    while A[i] >= 10:
      sum = 0
      for j in range(len(A[i])):
        sum += int(A[i][j])
    A[i] = int(A[i])
    if (A[i] == '0' or A[i] == '3' or A[i] == '6' or A[i] == '9') and (t[-1] == '0' or t[-1] == '5'):
      A[i] = 'fizzbuzz'
    elif (A[i] == '0' or A[i] == '3' or A[i] == '6' or A[i] == '9') and (t[-1] != '0' and t[-1] != '5'):
      A[i] = 'fizz'
    elif (A[i] != '0' and A[i] != '3' and A[i] != '6' and A[i] != '9') and (t[-1] == '0' or t[-1] == '5'):
      A[i] = 'buzz'
    else:
      A[i] = t
  return A

A = replace(['1', '2', '3', '4'])
print(A)
