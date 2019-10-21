import random

num_list = []
for i in range(5):
    num_list.append(random.randint(1, 20))

i = len(num_list) - 1

while i > 1:
    j = 0
    while j < i:
        if num_list[j] > num_list[j + 1]:
            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp
        else:
            print()

        j += 1

    i -= 1


print(num_list)