# ============================================================
# Step 1: Ask for Total Bill
# ============================================================



# ============================================================
# Step 2: Ask for Number of People
# ============================================================



# ============================================================
# Step 3: Calculate Equal Split
# ============================================================
# - Divide total bill by number of people
# - Store result in a variable
# ============================================================



# ============================================================
# Step 4: Print Final Result
# ============================================================
# - Print the result in this format:
#   Each person pays: $<amount>
#   Rounded to 2 decimal places
# ============================================================
total = input("Enter the total bill amount: ")
people = input("Enter the number of people: ")
average = float(total) / int(people)
print("each person pays: $" , round(average, 2))
# end of task 1