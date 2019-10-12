
some_str = "this is a very important string"

print(some_str[0])
print(some_str[0:4])
print(some_str[-1])
print(some_str[8:])

print("Len : ", len(some_str))

print("Hello Five Times \n" * 5)

# Convert Num to Str
number = 4
num_str = str(number)
print(type(num_str))

# Iterate each string to char
for char in some_str:
    print(char)

print("================ JUMP ITERATION ===============")
for i in range(0, len(some_str)-1, 2):
    print(some_str[i] + some_str[i+1])


# Convert STRING - UNICODE
# A - Z 65 - 90
# a - z 97 - 122

print("A = ", ord("A"))
print("95 = ", chr(65))