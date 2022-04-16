while True:
    a = input("檢測的字串(end結束):")
    if a == "end":
        break
    else:
        b = input("檢測的單一字元:")
        print("字元",b,"出現的次數為:",a.count(b))