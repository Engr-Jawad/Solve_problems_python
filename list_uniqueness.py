list=[]
size=int(input("enter the size of the list : "))
for i in range(size):
    element=input("enter the element :")
    list.append(element)
unique_list=set()
for item in list :
    if item in unique_list:
        print("the duplicate elements in the list are : ",unique_list)
        break
    unique_list.add(item)