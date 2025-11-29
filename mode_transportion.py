distance=float(input("enter the distance in km :"))
if distance > 0 and distance <= 5:
    print("go on walk")
elif distance > 5 and distance <=15:
    print("go on the bike")
elif distance > 15 and distance <=1000:
    print("go by car")
else:
    print("go by plane")