# Bagaimana jika kita tidak tahu jumlah parameter yang akan di masukkan user
# Gunakanlah *args


def jumlahkan_semua(*args):
    total = 0
    for i in args:
        total += i

    return total


print(jumlahkan_semua(1,2,3))




