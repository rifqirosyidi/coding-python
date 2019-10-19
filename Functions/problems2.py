# GENERATE Bilangan Prima
# Bil Prima : Hanya Bisa di bagi 1 dan dirinya sendiri, Contoh : 5 hanya bisa dibagi 1 dan 5
# Bukan Prima : Contoh 6 : bisa dibagi 1 ,2 ,3, 6


# Definisikan Fungsi sederhana untuk cek apakah bilangan tersebut prima contoh : is_prime(4)
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_prime(max_prime_num):
    list_bil_prima = []
    for num in range(2, max_prime_num):
        if is_prime(num):
            list_bil_prima.append(num)
    return list_bil_prima


max_input = int(input("Cari Bilangan Prima Sampai : "))
print("LIST ALL PRIME NUM: ", get_prime(max_input))
