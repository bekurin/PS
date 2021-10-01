# baekjoon No.1339 word math
n = int(input())

data = []
answer, count = 0, 9
data_dict, answer_dict = {}, {}

for i in range(n):
  data.append(list(map(str, input())))
  data[i].reverse()

for item in data:
  for i in range(len(item)):
    if data_dict.get(item[i]) is None:
      data_dict[item[i]] = 10 ** i;
    else:
      temp = data_dict.get(item[i])
      data_dict[item[i]] = temp + 10 ** i;
      
data_dict = sorted(data_dict.items(), key=lambda x: x[-1], reverse=True)

for item in data_dict:
  if answer_dict.get(item[0]) is None:
    answer_dict[item[0]] = count;
    count -= 1;

for item in data:
  temp_str = ''
  item.reverse()
  for i in range(len(item)):
    temp_str += str(answer_dict.get(item[i]))
  answer += int(temp_str)

print(answer)