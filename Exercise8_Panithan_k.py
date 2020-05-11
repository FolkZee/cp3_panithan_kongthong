usernameinput = input("user:")
passwordinput = input("passward:")
x = 1
A = 0
if usernameinput == "folk" and passwordinput == "1234":
    while x>=1:
        print("----welcome to 11-7----")
        print("cola x1            10 THB")
        print("fish and chips X1  60 THB")
        print("hamberger x1       50 THB")
        print("pork chop x1       50 THB")
        print("rib eye steak x1   80 THB")
        selectfood = input("select your foods>>")
        if selectfood == "cola":
            number = int(input("Amount of food>>"))
            number = number * 10
            A += number
            Choose = input("order(y) or checkout(n)>>")
            if Choose == "n":
                print("----Total----")
                print(":", A, "THB")
                x -= 1
            if Choose == "y":
                print("now:",A)
                x = 1
        if selectfood == "fish and chips":
            number = int(input("Amount of food>>"))
            number = number * 60
            A += number
            Choose = input("order(y) or checkout(n)>>")
            if Choose == "n":
                print("----Total----")
                print(":", A, "THB")
                x -= 1
            if Choose == "y":
                print("now:", A)
                x = 1
        if selectfood == "hamberger":
            number = int(input("Amount of food>>"))
            number = number * 50
            A += number
            Choose = input("order(y) or checkout(n)>>")
            if Choose == "n":
                print("----Total----")
                print(":", A, "THB")
                x -= 1
            if Choose == "y":
                print("now:", A)
                x = 1
        if selectfood == "pork chop":
            number = int(input("Amount of food>>"))
            number = number * 50
            A += number
            CChoose = input("order(y) or checkout(n)>>")
            if Choose == "n":
                print("----Total----")
                print(":", A, "THB")
                x -= 1
            if Choose == "y":
                print("now:", A)
                x = 1
        if selectfood == "rib eye steak":
            number = int(input("Amount of food>>"))
            number = number * 80
            A += number
            Choose = input("order(y) or checkout(n)>>")
            if Choose == "n":
                print("----Total----")
                print(":", A, "THB")
                x -= 1
            if Choose == "y":
                print("now:", A)
                x = 1


