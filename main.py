import random

def bubble_sort(number_list):
    for i in range(len(number_list)):
        for j in range(1, len(number_list) - i):
            if number_list[j-1] > number_list[j]:
                number_list[j-1], number_list[j] = number_list[j], number_list[j-1]
        print('step.{:2} list: {}'.format(i, number_list))
    return number_list


number_list = list(range(11))
random.shuffle(number_list)
print('origin list: {}'.format(number_list))

result = bubble_sort(number_list)
print('result list: {}'.format(result))
