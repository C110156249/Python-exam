a = int(input("請輸入第一個要判斷的數字:"))
b = int(input("請輸入第二個要判斷的數字:"))
s = 0
if a-b == 2 or b-a == 2:
    for i in range(2,a):
        if a%i == 0:
            s = s +1
    for j in range(2,b):
        if b%i == 0:
            s = s +1
    if s == 0:
        print("Y")
    else:
        print("N")
else:
    print("N")