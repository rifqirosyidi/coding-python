'''
1,2,3,4,5,6,7,8,9
2,4,6,8,10,12,14,16,18
3,6,9 ..
4,...
...
8, ...
9, ..
'''

list_math = [[i] * 10 for i in range(10)]

# Assign
for i in range(1, 10):
    for j in range(1, 10):
        list_math[i][j] = f'{i * j}'

# Outputing The Data
for i in range(1, 10):
    for j in range(1, 10):
        print(list_math[i][j], end=" | ")
    print()