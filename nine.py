s1=input("Enter first string:")
s2=input("Enter second string:")
ms=s1+s2
res=""
for ch in ms:
    if ch.isupper():
        res+=ch 
print("Merged result with only caps:",res)        