while True:
    try:
        number = int(input("Please Enter a Number : "))
        break
    except ValueError:
        print("You didn't Enter a Number")
    except:
        print("An unknown error occurred")
