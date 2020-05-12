def login():
    nameinput = input("name:")
    passwordinput = input("password:")
    if nameinput == "admin" and passwordinput == "1234":
        showmenu()
    else:
        print("wrong Try again")
        login()
def showmenu():
    print("-----UShop-----")
    print("1. Vat Calculate")
    print("2. Price Calculate")
    print(menuSelect())
def menuSelect():
    userSelct = int(input(">>"))
    if userSelct == 1:
        A = int(input("price:"))
        return VatCalculate(A)
    elif userSelct == 2:
        return Pricecalculate()
def VatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result
def Pricecalculate():
    price1 = int(input("First number:"))
    price2 = int(input("Second number:"))
    return VatCalculate(price1+price2)
login()

