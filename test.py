a = int(input())
b = int(input())
c = int(input())

cal = a+b+c 

if cal >= 80 and cal <=100:
    print("A")
elif cal >=75 and cal <=80:
    print("B+")
elif cal >=70 and cal <=75:
    print("B")
elif cal >=65 and cal <=70:
    print("C+")
elif cal >=60 and cal <=65:
    print("C")
elif cal >=65 and cal <=60:
    print("D+")
elif cal >=50 and cal <=55:
    print("D")
elif cal<=50:
    print("F")
else:
    print("Error score")
