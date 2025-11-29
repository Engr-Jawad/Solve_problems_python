marks=int(input("enter your marks : "))
if marks >=90 and marks <= 100 :
    grade = "A"
elif marks >=80 and marks < 90:
    grade ="b"
elif marks >= 70 and marks < 80 :
    grade = "C"
elif marks >=60 and marks < 70 :
    grade = "d"
elif marks < 60 :
    grade = "fail "
else: 
    grade = "invalid marks "

print("your grade is :",grade)