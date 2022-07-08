a = int(input())
array = []

for i in range(0,a):
  array.append(input())

result = []
for i in range(0, len(array)):
  length = len(list(str(array[i])))
  k = array[i]
  for j in range(1, length):
    if str(k)[length-j:length-j+1] == '5':
      k = str(int(k) + 10**(j-1))
    k = round(int(k),-j)
  result.append(k)

for i in range(0, len(result)):
  print(result[i])
