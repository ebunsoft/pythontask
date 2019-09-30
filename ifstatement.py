age = int(input("Enter your Age:"))

if ((age > 0) and (age < 13)):
    print("You're a Child")
elif((age > 13) and (age < 20)):
    print("You're an Adolescence")
elif(age > 19):
    print("You're an Adult")
else:
    print("Invalid Age Specified")
