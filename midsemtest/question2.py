# ============================================================
# Step 1: Ask for Starting Amount
# ============================================================



# ============================================================
# Step 2: Ask for Number of Days
# ============================================================



# ============================================================
# Step 3: Use a for loop to simulate savings
# ============================================================
# - Use range() correctly
# - Add the correct daily savings amount
# - Update and print the total each day
#   Day <X>: $<Y>
# ============================================================



# ============================================================
# Step 4: Print Final Total
# ============================================================
# - Print the final amount in this format:
#   Total amount saved = $<Z>
# ============================================================
start_amt = input("Enter the starting amount: ")
days = input("Enter the number of days: ")
for i in range(1, int(days) + 1):
    start_amt = float(start_amt) + i
    print("Day", i, ": $", (float(start_amt)))
print("total amount saved = $", (float(start_amt)))