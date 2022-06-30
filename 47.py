n=int(input("請輸入比數n:"))
a=[]
for i in range(n):
    a.append(input("輸入字典資料:").split(" "))
for i in range(n):
    print(f"{a[i][0]}牌得到{a[i][1]}面")


