a = [-3, 7, 12, 2, -8, 5]
N = len(a)

for i in range(0, N - 1):
  for j in range(0, N - 1 - i):
    if a[j] > a[j + 1]:
      a[j], a[j + 1] = a[j + 1], a[j]

print(a)