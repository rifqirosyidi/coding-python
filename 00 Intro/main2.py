# User menginputkan operasi aritmatik sederhana 5 + 9

# Simpan variable num1 dan num2 dan juga variabel operator
num1, operator, num2 = input("Masukkan Operasi : ").split()

# Convert numbers to int
num1 = int(num1)
num2 = int(num2)

# cek Operatornya
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))

elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))

elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))

else:
    print("Hanya menggunakan + - * /")
