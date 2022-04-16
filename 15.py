a = list(input("輸入一組四位數字為:"))
for i in range(4):
    a[i] = (int(a[i]) + 7) % 10
print("輸出加密後的數字為:",a[2],a[3],a[0],a[1])