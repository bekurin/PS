# baekjoon No.1759 암호 만들기
# l, c = map(int, input().split(' '))

# data_type = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

# data = list(input().split(' '))

l, c = 4, 6

data_type = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

data = ['a', 't', 'c', 'i', 's', 'w']
numeric_data = {}
for item in data:
  if data_type.get(item) is not None:
    temp = data_type.get(item)
    numeric_data[temp] = item

numeric_data.sort()
temp_str = ''
answer = []

for item in data:
  temp_str = ''
  while len(temp_str) < 4:
    for i in range(c):
      for j in range(i+1, c):
        if numeric_data[i] > numeric_data[j]:
          continue
        print(temp_str)
        temp_str += 'a'
        break



print(answer)
print(numeric_data)