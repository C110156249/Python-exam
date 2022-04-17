a = list(input("輸入自傳(至少10個字):"))
a.remove("，")
a.remove("。")
d = []
for i in range(len(a)):
    b = a.count(a[i])
    c = d.count(a[i])
    if b > 1 and c == 0:
        d.append(a[i])
print(d)