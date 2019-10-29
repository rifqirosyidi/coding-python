class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving Height...")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please enter number only!")

    @property
    def width(self):
        print("Retrieving Width...")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please enter numbers only!")

    def get_area(self):
        return int(self.__height) * int(self.__width)


def main():
    aSquare = Square()

    height = input("Enter Height : ")
    width = input("Enter Width : ")
    aSquare.height = height
    aSquare.width = width

    print("Height ", aSquare.height)
    print("Width ", aSquare.width)

    print("The Area is ", aSquare.get_area())


main()