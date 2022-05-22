t = int(input("請輸入T(總共有幾筆資料:)"))
list = []
for i in range(t):
    for j in range(4):
        a = int(input("請輸入數字:"))
        list.append(a)
    if list[3] - list[2] == list[2] - list[1] == list[1] - list[0]:
        list.append(list[3]+(list[3] - list[2]))
        print(list)
        print("此為等差數列")
    elif list[3] / list[2] == list[2] / list[1] == list[1] / list[0]:
        list.append(list[3]*round((list[3] / list[2])))
        print(list)
        print("此為等比數列")
    list.clear()