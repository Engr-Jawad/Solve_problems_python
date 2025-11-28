list=[]
size=int(input("enter the size fo the list : "))
for i in range(size):
    ele=int(input("enter the element : "))
    list.append(ele)
squard_list=[x ** 2 for x in list]
print("the squared of the list is  :",squard_list)