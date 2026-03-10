password=input("enter your password : ")
length=len(password)
if length < 6 :
    print("weak password")
elif length >= 6 and length <=10 :
    print("moderate")
else:
    print("strong password")
    