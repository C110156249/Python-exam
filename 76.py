a = (input("請輸入傳送密碼(6位數):"))
if len(a) < 6:
    print("密碼長度不足6個字元,請重新輸入")
else:
    a = list(a)
    a1 = int(a[0])
    a2 = int(a[1])
    a3 = int(a[2])
    a4 = int(a[3])
    a5 = int(a[4])
    a6 = int(a[5])
    b = ((a1*4)%7,(a2*4)%7,(a3*4)%7,(a4*4)%7,(a5*4)%7,(a6*4)%7)
    print("解密後的密碼:",b)