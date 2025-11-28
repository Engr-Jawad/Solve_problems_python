# mylist=[1,2,3,4,5,6,7,5,4,3,3,2,2,21,1,3,5,6,7]
# duplicatelist=[]
# for i in mylist:
#     if i not in duplicatelist:
#         duplicatelist.append(i)
# print("duplicate value remove from your list is = ",duplicatelist)
list=[]
size=int(input("enter the size of the list : "))
for i in range( size):
    ele=int(input("enter the element in the list  :"))
    list.append(ele)
duplicate=[]
for i in list :
    if i not in duplicate:
        duplicate.append(i)
print("duplicate remove from the list is : ",duplicate)