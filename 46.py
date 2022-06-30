n = int(input("請輸入比數n:"))
a = {}
for i in range(n):
    b,c = input("輸入字典資料:").split(" ")
    a[b] = c
for b,c in a.items():
    print("%s牌得到%s面"%(b,c))