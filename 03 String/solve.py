message = input("Masukkan Kata Yang Ingin di Enkripsi : ")
pergeseran = int(input("Berapa karakter yang ingin di geser (1 - 26) : "))

secret_message = ""

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += pergeseran

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        secret_message += chr(char_code)

    else:
        secret_message += char

print("Encrypted : ", secret_message)

orig_message = ""
pergeseran = -pergeseran

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += pergeseran

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        orig_message += chr(char_code)

    else:
        orig_message += char

print("Decrypted : ", orig_message)
