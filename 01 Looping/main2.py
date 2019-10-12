# While Loop

import random
randnum = random.randrange(0, 10)

i = 0

while i != randnum:
    i += 1

print("The Rand Val Is : ", i)


# Continue and Break
x = 1
while x < 20 :
    if x % 2 == 0:
       x += 1

    if x == 15:
        break

    print(x)
    x += 1