string=input("Enter string:")
count=0
for i in string:
    if i in ("AEIOUaeiou"):
        count+=1
print("Number of vowels in string are:"+str(count))        