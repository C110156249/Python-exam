n = int(input("請輸入整數n:"))
a = [n]
while n != 1:
    if n % 2 != 0:
        n = 3*n+1
    else:
        n = n//2
    a.append(n)
print(a,"n的cycle length=",len(a))