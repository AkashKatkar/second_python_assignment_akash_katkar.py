# Task 1: Check if a Number is Even or Odd

num = int(input("Enter a number: "))
if num == 0:
    print("The number is zero")
elif num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


print("\n")


# Task 2: Sum of Integers from 1 to 50 Using a Loop

print("for loop:")
num_sum = 0
for i in range(1, 51):
    num_sum += i

print(f"The sum of numbers from 1 to 50 is: {num_sum}")

print("\nwhile loop:")
num_sum = 0
i = 1
while i <= 50:
    num_sum += i
    i += 1

print(f"The sum of numbers from 1 to 50 is: {num_sum}")