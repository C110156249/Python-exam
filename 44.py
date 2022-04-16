t = int(input("輸入班級數:"))
a = []
for i in range(t):
    b = int(input("輸入每班人數:"))
    a.append(b)
print("須購買",max(a),"台電腦")