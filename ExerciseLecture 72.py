menulist = []
def showbill():
    print("----welcome----")
    sum = 0
    for number in range(len(menulist)):
        print(menulist[number][0],"x"+menulist[number][1],str(menulist[number][2])+"THB")
        sum += int(menulist[number][2])
    print("Total price =", sum, "THB")
while True:
    menuName = input("Please Enter Menu:")
    if menuName.lower() == "exit":
        break
    else:
        numberfood = input("Number:")
        menuprice = int(input("Prce:"))
        menulist.append([menuName,numberfood,menuprice])
showbill()

