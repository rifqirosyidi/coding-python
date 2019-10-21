import math


def get_luas_bidang(value):
    bidang = value.lower()
    if bidang == "segitiga":
        bidang_segitiga()
    elif bidang == "segiempat":
        bidang_segiempat()
    elif bidang == "lingkaran":
        bidang_lingkaran()
    else:
        print("Hanya Menangani Segitiga, Lingkaran dan Segiempat")


def bidang_segitiga():
    alas = float(input("Masukkan Alas : "))
    tinngi = float(input("Masukkan Tinggi : "))

    luas = (0.5 * alas) * tinngi
    print("Luas Segi Tiga : ", luas)


def bidang_segiempat():
    lebar = float(input("Masukkan Lebar : "))
    panjang = float(input("Masukkan Panjang : "))

    luas = panjang * lebar
    print("Luas Segi Empat : ", luas)


def bidang_lingkaran():
    jari_jari = float(input("Masukkan Jari Jari Lingkaran : "))

    luas = math.pi * math.pow(jari_jari, 2)
    print("Luas Lingkaran : ", round(luas, 2))


def main():
    bentuk_bidang = input("Masukkan Bidang Apa Yang Ingin di Hitung : ")
    get_luas_bidang(bentuk_bidang)


main()