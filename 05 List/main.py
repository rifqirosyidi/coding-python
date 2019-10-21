import math
import random

one_to_ten = list(range(10))
print(one_to_ten)

rand_list = [123, "Str", True]
print(rand_list)

concatenate_list = one_to_ten + rand_list
print(concatenate_list)

first_four_item = concatenate_list[:4]
print("First Four : ", first_four_item)

multi_last = concatenate_list[-2] * 5
print(multi_last)

print("List Length : ", len(concatenate_list))
print("Str in list? : ", "Str" in concatenate_list)
print("Index of Str : ", concatenate_list.index("Str"))
print("How many Str : ", concatenate_list.count("Str"))

# Changing List
concatenate_list[0] = "New String"
print("CHANGING LIST : ", concatenate_list)

# Append List - Tambahkan value di urutan terakhir list
concatenate_list.append("String Appended")
print(concatenate_list)

