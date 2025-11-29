age=int(input("enter your age : "))
day=input("enter the day  (sunday,monday,tuseday,friday,saturaday,wednesday,thurasday):")
day="wednesday"
price = 12 if age >= 18 else 5
if day.lower() == "wednesday":
    price-=2
print("the ticket price is : ",price)