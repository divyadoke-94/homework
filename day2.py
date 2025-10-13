#display the variable & name
car = ["BMW","AUDI","FERRARI","PORCHE"]

for i in car:
    print(i)

for i in range (5):
    print("hello")


# for loop
for i in range (2,6):
    print(i)

for i in "apple":
    print (i)



#while loop
i = 0
while i < 5:
    print("hello")
    i += 1



a = ["apple","mango","banana"]
print (a[0])


i = 0
while i < 5:
  print(5+7)
  i +=1


#practise questions
#leap year
year = int(input("Enter a year: "))


if (year % 4 == 0):
    if (year % 100 != 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#users prints

age = int(input("Enter your age: "))

if age >= 0:  
    if age <= 12:
        print("You are a Child.")
    else:
        if age <= 19:
            print("You are a Teenager.")
        else:
            if age <= 59:
                print("You are an Adult.")
            else:
                print("You are a Senior Citizen.")
else:
    print("Invalid age entered. Age cannot be negative.")



# Take input from the user
num = int(input("Enter a number: "))


for i in range(1, 11):  
    print(f"{num} x {i} = {num * i}")



# Initialize sum
total = 0

# Loop from 1 to 100
for num in range(1, 101):
    if num % 2 == 0:  # Check if number is even
        total += num  # Add even number to total

print("Sum of all even numbers from 1 to 100 is:", total)



#prime numbers using a for loop
for n in [2,3,4,5,6,7,8,9,10]:
    if n >1 :
        factors = 0
        for j in range(1, n+1):
            if n % j == 0:
                factors += 1
        if factors ==2:
            print(n)