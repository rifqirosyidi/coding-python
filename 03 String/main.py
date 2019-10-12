rand_string = "    this is an important string   "
rand_string = rand_string.strip()

print(rand_string.capitalize())

a_list = ['bunch', 'of', 'random', 'string']
print(" ".join(a_list))

split_rand_string = rand_string.split(" ")
for i in split_rand_string:
    print(i)

print("How many character 'is' : ", rand_string.count("is"))
print("Where is the char string : ", rand_string.find("string"))

# Replace String
print(rand_string.replace("an ", "a kind of "))