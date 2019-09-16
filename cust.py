cid=int(input("Enter customer id"))
name=input("Enter customer name")
bid=int(input("Enter bill id"))
bamt=int(input("Enter bill amount"))
if(len(name)>3 and len(name)<20):
    print("Customer details:")
    print("Name:"+name)
    print("Customer ID:"+str(cid))
    print("Bill ID:"+str(bid))
    print("Bill amount:"+str(bamt))
else:
    print("Invalid name")
        
    