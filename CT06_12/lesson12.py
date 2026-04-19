# print("Hello from lesson 12")

# recap
# game_status = input("Is the game active?(active/paused): ")
# if game_status == "active" or not (game_status == "paused"):
#     print("game is in progress")
# else:
#     print("game is paused")

# task 1
# import time
# numpplstart = int(input("Enter the number of people at the start: "))
# while numpplstart < 100000:
#     numpplstart += 1
#     print(numpplstart)
#     time.sleep(0.00001)

# task 2
# numpplstart = int(input("Enter the number of people at the start: "))
# while True:
#     if numpplstart == 100000:
#         break
#     numpplstart += 1
#     print(numpplstart)

# task 3
# order = ""
# endorder = ""
# while order != "done":
#     order = input("What would you like to order? (type 'done' to finish): ")
#     if order == "done":
#         print("Thank you for your order!")
#         print("(" ,endorder, ")")
#     else:
#         print(f"You have ordered: {order}")
#         endorder = endorder + order + ", "

# # task 4a
# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
# print("happy new year!")

# task 4b
# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
#     if i == 5:
#         break

# task 5a
# import random
# num1 = random.randint(1, 10)
# num2 = random.randint(1, 10)
# answer = int(input(f"What is {num1} + {num2}? "))
# if answer == num1 + num2:
#     print("Correct!")
# else:
#     print("Incorrect. The correct answer is", num1 + num2)

#      OR

# import random
# hidden = -1
# reply = 0
# while hidden == reply:
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     question = f"What is {num1} + {num2}?"  
# #    print(question)
#     reply = input(question)
#     reply = int(reply)
#     if hidden == reply:
#         print("Correct!")
#     else:
#         print("Incorrect. The correct answer is", num1 + num2 , ". Try another question.")
# task 5b
# score = 0
# for i in range(15):
#     import random
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     answer = int(input(f"What is {num1} + {num2}? "))
#     if answer == num1 + num2:
#         print("Correct!")
#         score += 2
#     elif answer != num1 + num2:
#         print("Incorrect. The correct answer is", num1 + num2)
#         score -= 1
#     elif answer == "skip":
#         print("Question skipped.")
# print("Your final score is:", score)

# task 6
# ranum = 0
# counter = 0
# import random
# num = 4
# while not ranum == num:
#     ranum = random.randint(1, 6)
#     counter += 1
# print(f"It took {counter} rolls to get a {num}.")