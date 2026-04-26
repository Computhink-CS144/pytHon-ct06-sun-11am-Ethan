# print("Hello from lesson 13")

# Recap 1
# amt = 1000
# while True:
#     change = input("Do you want to withdraw, deposit, check your balance , or exit? (w/d/cb/e): ")
#     if change == "w" or change == "withdraw":
#         withdraw_amt = int(input("How much do you want to withdraw? "))
#         if withdraw_amt > amt:
#             print("You don't have enough money to withdraw that amount.")
#         else:
#             amt -= withdraw_amt
#             print(f"You have withdrawn {withdraw_amt}. Your new balance is {amt}.")
#     elif change == "d" or change == "deposit":
#         deposit_amt = int(input("How much do you want to deposit? "))
#         amt += deposit_amt
#         print(f"You have deposited {deposit_amt}. Your new balance is {amt}.")
#     elif change == "cb" or change == "check balance":
#         print(f"Your current balance is {amt}.")
#     elif change == "e":
#         print(f"Thank you for using our services. Goodbye! Your balance is {amt}.")
#         break
# print("End")

# Task 1a
("add apples, bread, carrots, dates, eggs, flour, grapes and honey to your grocery list.")
groceries = []
groceries.append(input("Enter a grocery item: "))
continue_adding = input("Do you want to add another item? (y/n): ")
while continue_adding == "y":
    groceries.append(input("Enter a grocery item: "))
    continue_adding = input("Do you want to add another item? (y/n): ")
print("Your grocery list:")
for item in groceries:
    print(item)

# Task 1b
what_to_delete = input("Do you want to delete an item from your grocery list? (y/n): ")
while what_to_delete == "y":
    item_to_delete = input("Enter the item you want to delete: ")
    if item_to_delete in groceries:
        groceries.remove(item_to_delete)
        print(f"{item_to_delete} has been removed from your grocery list.")
    else:
        print(f"{item_to_delete} is not in your grocery list.")
    what_to_delete = input("Do you want to delete another item from your grocery list? (y/n): ")
print("Your updated grocery list:")
for item in groceries:
    print(item)
what_to_add = input("Do you want to add another item to your grocery list? (y/n): ")
while what_to_add == "y":
    groceries.append(input("Enter a grocery item: "))
    what_to_add = input("Do you want to add another item to your grocery list? (y/n): ")
print("Your final grocery list:")
for item in groceries:
    print(item)

# Task 1c
print("you just ran out of ice. Add ice to your list!")
groceries.append(input("Enter the item you want to add(ice): "))
print("Your updated grocery list:")
for item in groceries:
    print(item)
print("you also need some bananas. Add bananas inbetween the first and second item on your list.")
groceries.insert(1, input("Enter the item you want to add(bananas): "))
print("Your updated grocery list:")
for item in groceries:
    print(item)

# Task 1d
print("you don't want bread anymore. Delete bread!")
item_to_delete = input("Enter the item you want to delete(bread): ")
if item_to_delete in groceries:
    groceries.remove(item_to_delete)
    print(f"{item_to_delete} has been removed from your grocery list.")