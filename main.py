son =int(input("sonni kiriting"))
if son < 0:
    son1 = son + 1
    print(son1)
else:
    print(son)



son = int(input("sonni kiriting"))
if son <0:
    son1 = son + 1
    print(son1)
else:
    son2 = son1 / 2
    print(son2)



son = int(input("sonni kiriting -"))
if son <0:
    son1 = son + 1
    print(son1)
elif son == 0:
    son3 = son + 10
    print(son3)
else:
    son2 = son / 2
    print(son2)




son1 = int(input("sonni kiriting -"))
son2 = int(input("sonni kiriting -"))
son3 = int(input("sonni kiriting -"))
print((son1 <0) + (son2 <0) + (son3 <0))



son1 = int(input("sonni kiriting -"))
son2 = int(input("sonni kiriting - "))
son3 = int(input("sonni kiriting - "))
print("musbat son",(son1 < 0) + (son2 < 0) + (son3 < 0))
print("manfiy son",(son1 > 0) + (son2 > 0) + (son3 > 0))



son1 = int(input("birinchi sonni kiriting = "))
son2 = int(input("ikkinchi sonni kiriting = "))
if son1 > son2:
    print("birinchi son katta -",son1)
else:
    print("ikkinchi son katta -",son2)




son1 = int(input("birinchi sonni kiriting - "))
son2 = int(input("ikkinchi sooni kiriting - "))
if son < son2:
    print("birinchi son katta - ",son1)
else:
    print("birinchi son katta - ",son2)



son1 = int(input("birinchi sonni kiriting = "))
son2 = int(input("ikkinchi sonni kiriting = "))
if son1<son2:
    print("birinchi son kichik = ",son1)
    print("ikkinchi son katta = ",son2 )




ason = int(input("birinchi sonni kiriting = "))
bson = int(input("ikkinchi sonni kiriting = "))
if ason > bson:
    ason = bson
    print("a =",ason,"b = ",bson)
elif ason ==bson:
    ason = bson -1
    print("a = ",ason,"b = ",bson)


a = int(input(" a sonni kiriting -"))
b = int(input("b sonni kiriting - "))
if a==b:
    print("natija - 0",)
else:
    m = a + b
    print("natija -",m)



a = int(input("a sonni kiriting -"))
b = int(input("b sonni kiriting - "))
if a ==b:
    print("natija - 0",)
elif a<b:
    print("a katta",a)
elif a>b:
    print("b katta",b)
else:
    m = a + b
    print("natija -",m)