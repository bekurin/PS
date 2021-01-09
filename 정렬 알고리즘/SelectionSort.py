array = [1,5,2,3,4]

for i in range(len(array)):
  minIndex = i;
  for j in range(i+1, len(array)):
     if array[minIndex] > array[j]:
        minIndex = j
  array[i], array[minIndex] = array[minIndex], array[i]

print(array)
