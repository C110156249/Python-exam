a =int(input("a:"))
b =int(input("b:"))
c =int(input("c:"))
d = (((-b)+((b*b)-(4*a*c))**0.5)/(2*a))
e = (((-b)-((b*b)-(4*a*c))**0.5)/(2*a))
if (b*b)-(4*a*c) < 0:
    print("無解")
elif (b*b)-(4*a*c) == 0:
    print("%.0f"%d)
else:
    print("%.0f"%d)
    print("%.0f"%e)