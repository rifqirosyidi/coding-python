# Umur 0 - 5 -> Terlalu kecil untuk Sekolah
# Umur 6 - 12 -> Pergi ke SD print => SD Kelas 1 - SD Kelas 6
# Umur 13 - 15 -> Pergi ke SMP print => SMP Kelas 1 - SMP Kelas 3
# Umur 16 - 18 -> Masuk SMA

# Jika Mampu selesaikan tidak kurang dari 14 baris

umur = eval(input("Masukkan Umur : "))
if umur <= 5:
    print("Terlalu kecil untuk Sekolah")
elif 6 <= umur <= 12:
    kelas = umur - 5
    print(f'SD Kelas {kelas}')
elif 13 <= umur <= 15:
    kelas = umur - 12
    print(f'SMP Kelas {kelas}')
elif 16<= umur <= 19:
    print("Masuk SMA")
else:
    print("Masuk Kuliah")

