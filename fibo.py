terms=eval(input("Enter number of terms:"))
print("Fibonacci series is:")
if terms<=0:
    print()
elif terms==1:
    print("0")
else:
    a,b=0,1
    print(a,b,end=" ")
    for i in range(terms-2):
        print(a+b,end=" ")
        a,b=b,a+b
        