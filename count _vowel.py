("-----------||||||||||||||||||||||---------print------")

print("WELCOME TO VOWEL COUNT PROGARM  IN A  STRING ")
("-----------||||||||||||||||||||||---------print------")
st=input("enter string : ")
count = 0
for character in st:
    if (character in "aeiouAEIOU"):
       count+=1
       
       
print("COUNT : ",count)