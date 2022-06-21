n = int(input("輸入整數n:"))
for i in range(n//2+1):
        print(' '*(n-i)+'*'*(2*i-1))
for j in range(n//2+1,0,-1):
        print(' '*(n-j)+'*'*(2*j-1))