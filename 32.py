m = int(input("小明身上有幾元:"))
n = int(input("販賣機有幾種飲料:"))
a = 0
for i in range(n):
    p = int(input("飲料價格:"))
    if m >= p:
        a = a + 1
print("小明可以購買",a,"種飲料")