eid=int(input("Enter employee ID:"))
bsal=int(input("Enter Basic salary:"))
allow=int(input("Enter allowances:"))
gp=bsal+allow
if gp>20000:
    it=gp*0.3
elif gp>10000:
    it=gp*0.2
elif gp>5000:
    it=gp*0.1
else:
    it=0
np=gp-it
print("Employee details:")
print("ID:"+str(eid))    
print("Basic salary:"+str(bsal)) 
print("Allowances:"+str(allow))
print("Gross pay:"+str(gp))
print("Net pay:"+str(np))
                 