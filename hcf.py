a=(int(input("Enter a")))
b=(int(input("Enter b")))
while(b!=0):
    r=a%b
    a=b
    b=r
print("HCF is "+str(r))    
