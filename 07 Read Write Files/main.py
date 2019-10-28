import os

# Benefits storing data in other file is can be reused even if program is stopped

# mode w rewrite anything that is inside
# mode a append new line of text

with open("my_data.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Random Text\nMore Random\nSome More")

# mode by default is r (read)
with open("my_data.txt", encoding="utf-8") as myFile:
    # it have read() # return all str
    # readline()  # return str until new line
    # readlines() # return str list separated by new line

    print(myFile.read())


print(myFile.closed)
print(myFile.name)
print(myFile.mode)

# OS MODULE FUNC

# os.rename("old_name", "new_name")
# os.remove("my_data.txt")
# os.mkdir("new_dir")
# os.chdir("new_dir")
# os.getcwd()  # Get Current Working Dir
# os.rmdir("new_dir")


