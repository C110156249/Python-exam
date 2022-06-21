n = int(input("請輸入正整數n:"))
s = 0
for i in range(1,n):
    if n%i == 0:
        s = s + i
if s == n:
    print("perfect")
elif s > n:
    print("adundant")
elif s < n :
    print("defieient")