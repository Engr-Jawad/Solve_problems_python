list=[]
size=int(input("enter size of the list: "))
for i in range(size):
    element=int(input("enter element in the list : "))
    list.append(element)
reversedd=[]
for i in (list):
    reversedd = [i] + reversedd
print("reversed list is  : ",reversedd)