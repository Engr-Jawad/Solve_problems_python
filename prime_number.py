number=int(input("enter the number :"))
for i in range(2 ,number):
    if number % i == 0:
       print("not a prime numbr ")
       break
        
else:
    print("prime number")
    