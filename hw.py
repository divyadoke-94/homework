
#11111111111111111111
num = 1

# Loop until num exceeds 10
while num <= 10:
    print(num)
    num += 1  # Increment num by 1


#22222222222222222222222
# Take input from the user
num = int(input("Enter a number: "))

# Initialize variables
reverse = 0
temp = num

# Loop to reverse the number
while temp > 0:
    digit = temp % 10       # Get the last digit
    reverse = reverse * 10 + digit  # Append digit
    temp = temp // 10       # Remove last digit

print(f"Reversed number of {num} is {reverse}")

#333333333333333333333333
correct_password = "admin123"

while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break  # Exit the loop when password is correct
    else:
        print("Incorrect password, try again.")
