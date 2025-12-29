no=int(input("Enter the whole number: "))
sum=0
for i in range(1,no+1):
    sum=sum+i
print(f"The sum of the {i} is {sum}")


string = input("Enter a string: ")

string2 = ("")

for char in string:
    string2 = char + string2
print(f"Thhe original string is: {string}")
print(f"The reversed string is: {string2}")