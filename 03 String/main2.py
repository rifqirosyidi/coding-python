char_z = "z"
num_3 = "3"
space = " "


print("cek apakah z string atau number? : ", char_z.isalnum())
print("cek apakah z string? : ", char_z.isalpha())

print("cek apakah 3 number? : ", num_3.isdigit())

print("cek apakah z uppercase : ", char_z.isupper())
print("cek apakah z uppercase : ", char_z.islower())

print("cek apakah spasi spasi? : ", space.isspace())


num_phy = "3.14"


def apakah_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False


print("apakah pi number? : ", apakah_float(num_phy))



