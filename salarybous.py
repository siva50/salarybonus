salary = int(input("enter your salary"))
service = int(input("How many years of your service on your company"))
if service>10:
    bonus = 0.1*salary
    print("your net bonus amount is",bonus)
elif service>=6 and service<=10:
    bonus = 0.08*salary
    print("your net bonus amount is",bonus)
elif service<6:
    bonus = 0.05*salary
    print("your net bonus amount is",bonus)
else:
    print("your salary generated due to your service")


