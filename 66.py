a = set(input("請輸入string_a:"))
b = set(input("請輸入string_b:"))
if len(a&b) == 0:
    print("N")
else:
    c = (a&b)
    c1 = list(c)
    c1.sort()
    c = "".join(c1)
    print(c)