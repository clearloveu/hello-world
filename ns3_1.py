import math
from decimal import *
import matplotlib.pyplot as plt
print("求此公式：(4/(8*j+1)-2/(8*j+4)-1/(8*j+5)-1/(8*j+6))/16**j在j趋向于无穷时从j=0求和的值")
getcontext().prec=500
print("模拟j从1到50不同的求和的值")
x,y=[],[]
for i in range(1,51):
    a=0
    x.append(i)
    for j in range(i):
        a += Decimal((4 / (8 * j + 1) - 2 / (8 * j + 4) - 1 / (8 * j + 5) - 1 / (8 * j + 6)))/Decimal(16**j)
    a=float(a)
    y.append(a)
plt.plot(x,y)
plt.show()


while True:
    i=input("设置整数j的值为：")
    try :
        k=int(i)
    except TypeError :
        print("输入的不是整数")
    a=0
    for j in range(0,k+1):
        a += Decimal((4 / (8 * j + 1) - 2 / (8 * j + 4) - 1 / (8 * j + 5) - 1 / (8 * j + 6)))/Decimal(16**j)
    b=str(a)
    print("当j=%s的时候公式的值为："%j,b)
    for i in range(10):
        num=0
        for j in b:
            if j==".":
                continue
            d=int(j)
            if d==i:
                num+=1
        print("数字%s出现的丰度为%s"%(i,num))
    confirm=input("确认是否退出程序（输入Y即推出，其他任意键继续）：")
    if confirm=="Y":
        break




                  


