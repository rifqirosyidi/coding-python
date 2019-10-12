num_1, num_2 = input("enter two number sep by (space): ").split()

# convert dari strint to int
int_1 = int(num_1)
int_2 = int(num_2)

# Basic Aritmathic
addition = int_1 + int_2
substract = int_1 - int_2
division = int_1 / int_2
multiply = int_1 * int_2
remainder = int_1 % int_2
power = int_1 ** int_2

print(f"{int_1} + {int_2} = ", addition)
print(f"{int_1} - {int_2} = ", substract)
print(f"{int_1} / {int_2} = ", division)
print(f"{int_1} * {int_2} = ", multiply)
print(f"{int_1} % {int_2} = ", remainder)
print(f"{int_1} ^ {int_2} = ", power)


