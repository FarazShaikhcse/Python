string=input("Enter string:")
print("Original String:",string)
res=""
for ch in string:
    if ch not in "!@#$%^&*()_-=+{}[]<>,./?';:\|":
       res+=ch 
print("String without punctuations:"+res)       