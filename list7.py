print("from 2010 to 2020")
for i in range(2010,2021):
    if i%4==0 and i%100!=0 or i%400==0:
         days=366
    else:
         days=365
    print("year",i,"=",days,"days")              