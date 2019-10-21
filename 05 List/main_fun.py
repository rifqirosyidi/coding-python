import random

num_list = []
for i in range(10):
    num_list.append(random.randint(1, 20))

# num_list.sort()
# num_list.reverse()

num_list.insert(4, 1)
num_list.remove(1)

print(num_list)