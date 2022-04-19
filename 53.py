n = int(input("輸入n值:"))
dict1 = {}
for i in range(n):
    a = input("請輸入姓名:")
    b = input("請輸入電子郵件:")
    dict1.setdefault(a,b)
c = input("請輸入要查詢電子郵件的姓名:")
print(c,"電子郵件帳號為:",dict1[c])