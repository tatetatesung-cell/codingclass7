a = "gfdh"
b = "huisdrfgm"

if (a in b) :
    print(True)
else:
    print(False)

a = 5
b = 10

print("a >> 1 =", a >> 1)
print("b << 2 =", b << 2)


mark1 = int(input("Enter mark1: "))
mark2 = int(input("Enter mark2: "))
mark3 = int(input("Enter mark3: "))
mark4 = int(input("Enter mark4: "))
mark5 = int(input("Enter mark5: "))
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5
print(f"Total: {total}, Average: {average}")

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")
