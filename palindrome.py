st = input()
rev = ''
for char in st:
    rev = char + rev
if st == rev:
    print("string is palindrome")
else:
    print("string is not palindrome")