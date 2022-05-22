t = int(input("請輸入搭了幾次電梯:"))
sum = 0
b = 1
for i in range(t):
    a = int(input("請輸入樓層:"))
    if a > b:
        sum = sum + (a-b)*20
    else:
        sum = sum + (b-a)*10
    b = a
print(sum)