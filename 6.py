a = (input("輸入值為:"))
a = a.split(" ")
a.sort()
b = a
b1 = "".join(b)
a.sort()
a.reverse()
c = a
c1 = "".join(c)
print(int(c1)-int(b1))
