s = {}
n = int(input("輸入筆數n:"))
for i in range(n):
    a = input("輸入英文")
    b = input("輸入中文")
    s.setdefault(a,b)
c = input("輸入欲查詢單字:")
print(c + "中文意思為" + s.get(c))