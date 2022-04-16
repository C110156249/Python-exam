n = int(input("組數為:"))
for i in range(1,n+1):
    a = list(input("第組:"))
    print("第",i,"組應收費用:",int(a[0])*250+int(a[1])*175)