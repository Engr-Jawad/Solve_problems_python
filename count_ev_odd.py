# list=[]
# size=int(input("enter the size of list :"))
# for i in range(size):
#     element=int(input("enter the element :"))
#     list.append(element)
# even_count=0
# odd_count=0
# i=0
# while i < len(list):
#     for i in range(len(list) ):
#         if i % 2 ==0:
#             even_count+=1
            
#         else:
#             odd_count+=1
#         i+=1
#     print("even count : ",even_count,"odd count : ",odd_count)
    
    # Program to count even and odd numbers in a list using a while loop

# Take input: a list of integers (space-separated)
lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Initialize counters
even_count = 0
odd_count = 0

# Initialize index for while loop
i = 0

# Use while loop to iterate through the list
while i < len(lst):
    if lst[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

# Print the results
print(f"Even: {even_count}, Odd: {odd_count}")
