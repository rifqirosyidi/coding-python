# Real World Object : Attribute & Capabilities
# Cat Attribute (Field) : Height, Weight, Favorite Food
# Cat Capabilities (Method) : Walk, Run, Eat


class Cat:

    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def walk(self):
        print("{} Cat is walk".format(self.name))

    def run(self):
        print("{} Cat is run".format(self.name))

    def eat(self):
        print("{} Cat is eat".format(self.name))


def main():
    kats = Cat("kats", 20, 40)
    kats.run()

main()


