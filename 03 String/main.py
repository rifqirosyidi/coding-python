rand_string = "    this is an important string   "
l_string = rand_string.lstrip()
r_string = rand_string.rstrip()
rand_string = rand_string.strip()  # remove white space

print(rand_string.capitalize())  # Capitalize first char

a_list = ['bunch', 'of', 'random', 'string']
print(" ".join(a_list)) # join a list as a string

split_rand_string = rand_string.split(" ")
for i in split_rand_string:
    print(i)

print("How many character 'is' : ", rand_string.count("is"))
print("Where is the char string : ", rand_string.find("string"))

# Replace String
print(rand_string.replace("an ", "a kind of "))