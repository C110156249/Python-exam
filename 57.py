a = {"1":72,"2":62,"3":82,"4":44,"5":60}
b = {"A":55,"B":68}
q1 = input("請選擇主餐及升級的套餐:(以空白鍵區隔)")
q2 = input("是否升級成大杯飲料:")
q3 = input("是否換成大薯:")
q = q1.split()
sum = a[q[0]]+b[q[1]]
if q2 == "是":
    sum = sum + 7
if q3 == "是":
    sum = sum + 13    
print("總共為",sum,"元")