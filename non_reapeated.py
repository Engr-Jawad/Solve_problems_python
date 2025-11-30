str=input("enter string :")
for i in str:
    if str.count(i) == 1:
        print("the first non reapeated character in the string is :: ",i)
        break
   