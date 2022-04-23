a = []
for i in range(10):
    b = int(input("請輸入第%.0f個數字:" %(i+1)))
    a.append(b)
a.sort()
print("最大的3個數字為:",a[9],a[8],a[7])
print("最小的3個數字為:",a[2],a[1],a[0])