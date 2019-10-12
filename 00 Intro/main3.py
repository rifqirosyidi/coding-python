
# Contoh Umur
umur = eval(input("Masukkan Umur Anda : "))

# 1 - 17 Are Important
if (umur >= 1) and (umur <= 17):
    print("Rayakan Ulang Tahun")

# 25 atau 50 Are Important
elif (umur == 25) or (umur == 50):
    print("Rayakan Ulang Tahun")

# if more than 65
elif umur > 65:
    print("Rayakan Ulang Tahun")

else:
    print("Jangan Rayakan Ulang Tahun")

