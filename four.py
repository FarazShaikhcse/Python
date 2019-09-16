a=(int(input("Enter a")))
b=(int(input("Enter b")))
c=(int(input("Enter c")))
a=a*a
b=b*b
c=c*c
if(a==b+c or b==a+c or c==a+b):
    print("Right angle triangle")
else:
    print("Not a Right angle triangle")    