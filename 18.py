a = []
for i in range(5):
    b = input("輸入牌:")
    if b == "A":
        b = 1
    if b == "J":
        b = 11
    if b == "Q":
        b = 12
    if b == "K":
        b = 13
    a.append(b)
print(int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4]))