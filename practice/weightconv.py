weight = input("Enter weight >>>")
units = input("(L)bs or (K)g")
if units.upper() == "K" :
    value = float(weight) * 2.20462262185
    print("your " + str(value) + "Lbs")
elif units.upper() == "L" :
    value = float(weight) * 0.45359237
    print("your " + str(value) + "Kgs")
else:
    print("try later....")