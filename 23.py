while True:
    n = int(input("輸入值n為:"))
    if n == -1:
        break
    else:
        print(round((n*n*n)/3,1))