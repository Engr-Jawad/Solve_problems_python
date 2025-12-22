age=int(input("enter your age : "))
if age > 0 and age < 13 :
    print("child")
elif age >=13 and age < 20 :
    print("teenage")
elif age >= 20 and age < 65 :
    print("adult")
else :
    print("senior")
print("thank you")