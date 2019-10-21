import random
import math

list_of_tables = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        list_of_tables[i][j] = f'{i}, {j}'

for i in range(4):
    for j in range(4):
        print(list_of_tables[i][j], end=" | ")
    print()





