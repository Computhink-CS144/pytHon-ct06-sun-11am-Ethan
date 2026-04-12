# print("Hello from lesson 10")

#          recap 
# import random
# randint = random.randint(1, 15)
# guess = int(input("Guess a number between 1 and 15: "))
# if guess == randint:
#     print("Congratulations! You guessed the number.")
# else:
#     print(f"Sorry, the number was {randint}. Better luck next time!")

#           task 1
# num = input("Enter a number: ")
# if (int(num) > 0):
#     print("The number is positive.")
# else:
#     print("The number is negative.")

#           task 2
# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are a child.")
# else:
#     if age < 20:
#         print("You are a teenager.")
#     else:
#         print("You are an adult.")

#           task 3
# OUTSIDE_TEMP = int(input("Enter the outside temperature in degrees Celsius: "))
# if OUTSIDE_TEMP < 20:
#     print("It's cold outside. just read a book.")
# elif OUTSIDE_TEMP < 24 and OUTSIDE_TEMP >= 20:
#     print("It's a nice day outside. Let's go and cycle.")
# elif OUTSIDE_TEMP < 30 and OUTSIDE_TEMP >= 25:
#     print("let's play basketball outside.")
# else:
#     print("It's too hot outside. Let's go swimming.")

#          task 4
# score = int(input("Enter your score: "))
# if score >= 90:
#     print("Your grade is A.")
# elif score >= 80 and score < 90:
#     print("Your grade is B.")
# elif score >= 70 and score < 80:
#     print("Your grade is C.")
# elif score >= 60 and score < 70:
#     print("Your grade is D.")
# else:
#     print("Your grade is F.")

#                    OR
# score = int(input("Enter your score: "))
# if score in range(90, 101):
#     print("Your grade is A.")
# elif score in range(80, 90):
#     print("Your grade is B.")
# elif score in range(70, 80):
#     print("Your grade is C.")
# elif score in range(60, 70):
#     print("Your grade is D.")
# else:
#     print("Your grade is F.")