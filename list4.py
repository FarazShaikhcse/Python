n=int(input("enter the no of elements"))
l=[]
print("enter elements")
for i in range(1,n+1):
     a=input()
     l.append(a)
key=int(input("enter key element"))
beg=0
end=n-1
while(beg<=end):
    mid=(beg+end)//2
    if int(l[mid])==key:
        print("key found at "+str(mid+1))
        exit(0)
    elif int(l[mid])<key:
        beg=mid+1   
    else:
        end=mid-1  
print("key not found")