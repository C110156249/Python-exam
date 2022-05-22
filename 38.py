n = int(input("輸入小狗可能跑到幾個地方:"))
a = []
for i in range(n):
    k = int(input("輸入猜想的點與家的距離"))
    a.append(k)
sum = 0
for i in range(len(a)):
    if a[i] % 9 == 0 or a[i] % 11 == 0:
        sum += 1
        print("第",i+1,"個點",a[i])
if sum == 0:
    print(0)