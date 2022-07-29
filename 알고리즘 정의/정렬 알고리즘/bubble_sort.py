import random

def bubble_sort(number_list):
    for i in range(len(number_list)):
        for j in range(i, len(number_list)):
            if number_list[i] < number_list[j]:
                number_list[i], number_list[j] = number_list[j], number_list[i]
    return number_list


number_list = list(range(21))
random.shuffle()
print(bubble_sort(bubble_sort(number_list)))