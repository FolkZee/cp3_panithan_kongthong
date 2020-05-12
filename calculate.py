def vatcalculate(total):
    result = total+(total*7/100)
    return result
B = int(input(":"))
print(vatcalculate(B))

