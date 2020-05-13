menulist = []
pricelist = []
numberlist = []
def showbill():
    print("----welcome----")
    for number in range(len(menulist)):
        print(menulist[number],"x"+numberlist[number],str(pricelist[number])+"THB")
def totalbill():
    y = 0
    for x in pricelist:
        y = y + x
    print("ToTal>>",y,"THB")
while True:
    menuName = input("Please Enter Menu:")
    if menuName.lower() == "exit":
        break
    else:
        numberfood = input("Number:")
        menuprice = int(input("Price:"))
        menulist.append(menuName)
        pricelist.append(menuprice)
        numberlist.append(numberfood)
showbill()
totalbill()
