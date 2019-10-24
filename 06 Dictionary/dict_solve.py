# Buat List Kosong
list_users = []

# Gunakan While Loop
while True:

    # Buat Variabel Untuk Menyimpan Jawaban User (Y/N)
    buat_user = input("Masukkan User Baru (Y/N) : ")
    buat_user.lower()

    if buat_user == 'n':
        break

    else:
        nama_depan, nama_belakang = input("Masukkan Nama User (Hanya Nama Depan dan Nama Belakang) : ").split()
        list_users.append({'nama_depan': nama_depan, 'nama_belakang': nama_belakang})

# Print The Data
for user in list_users:
    print(user['nama_depan'], user['nama_belakang'])

