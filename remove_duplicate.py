mylist=[1,2,3,4,5,6,7,5,4,3,3,2,2,21,1,3,5,6,7]
duplicatelist=[]
for i in mylist:
    if i not in duplicatelist:
        duplicatelist.append(i)
print("duplicate value remove from your list is = ",duplicatelist)