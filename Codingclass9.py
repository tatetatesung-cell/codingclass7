medical_cause = input("Did you have a medical cause for missing classes? (yes/no): ")
attendance = int(input("Enter your attendance rate of the student: "))

if medical_cause == "yes":
    print("You are allowed.")
else:
    if attendance >= 75:
        print("You are allowed.")
    else:
        print("You are not allowed.")