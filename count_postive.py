num_list=int(input("enter size of the list :"))
count= 0
for  i in range (num_list):
    num=int(input("enter the number : "))
    if num > 0:
        count +=1
print("positive number in the list is : ",count)
    