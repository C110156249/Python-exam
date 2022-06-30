a = input("輸入N及M為:")
a = a.split(' ')
N = a[0]
M = [1]
b = input("輸入正矩陣第一列為:")
b = b.split(' ')
c = input("輸入正矩陣第二列為:")
c = c.split(' ')
for i in range(0,3):
    print("輸出陣列數值第" + str(i + 1) + "列為:" + b[i] + " " + c[i])
