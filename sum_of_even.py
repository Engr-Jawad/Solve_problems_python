num=int(input("enter a number : "))
sum=0
for i in range (num+1):
    if i % 2 == 0:
        sum+=i
print("the sum of even number is  :",sum)