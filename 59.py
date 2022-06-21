a = int(input("輸入金額"))
b = 0
while a > 0:
    if a >= 100:
        b = b + (a//100)
        a = a-((a//100)*100)
    elif a >= 50:
        b = b + (a//50)
        a = a-((a//50)*50)
    elif a >= 10:
        b = b + (a//10)
        a = a-((a//10)*10)
    elif a >= 5:
        b = b + (a//5)
        a = a-((a//5)*5)
    elif a >= 1:
        b = b + a
        a = 0
print(b)