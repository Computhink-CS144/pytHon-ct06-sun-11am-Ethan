
# Lesson 10 - If-Else Statements

# Recap 1: Random Number Guesser
**Recap 1a**:
Draw out the flowchart (on draw.io) of a program for the
user to guess a magic number.

Your program will need to:
1. Generate a random integer between 1 to 15
2. Ask the user to guess a number
3. If the user guesses correctly:
    print "That's it!"

**Recap 1b**:
Translate the flowchart that you have written for the
program into Python code.

-------------------------------------------------------------------

# Task 1: Positive or Negative Numbers
Write a program that will let the user know if the number they
have entered is positive or negative.

1. Ask the user to input a number
2. Using an 'if' statement, check if the number is greater than 0
        If it is, print "{number} is positive."
3. Use an 'else' statement for when the number is not greater than 0.
        In this case, print "{number} is negative."

-------------------------------------------------------------------

# Task 2: Simple Age Checker (nested if..else)​
Using nested ‘if…else’ conditions, write a program that categorises a person’s age as ‘Child’, ‘Teen’, or ‘Adult’.​

1. Initialise an ‘age’ variable and ask user for their age.​
2. Use an ‘if’ statement to check if the age is less than 13.​
- If true, print ‘Child’​
3. Within the ‘else’ statement of the 1st ‘if’ statement, use another ‘if’ statement to check if the age is between 13 and 19.​
- ​If true, print ‘Teen’​
- Else:​
- ​Print ‘Adult’​

-------------------------------------------------------------------

# Task 3: Activity Advisor ​
Using if...elif...else statements, write a program that suggests an activity based on the temperature: ​
1. Suggest swimming if temperature is above 30 degrees​
2. Suggest basketball if temperature is between 25 and 30 degrees​
3. Suggest cycling if temperature is between 20 and 24 degrees​
4. Suggest reading indoors if temperature is below 20 degrees​

Steps:​
1. Initialise a ‘temperature’ variable and ask user for temperature​
2. The order of your condition matters! Here's the pseudocode example:​

-------------------------------------------------------------------

# Task 4: Grading System
Implement a grading system where grades are assigned as
follows:​
- ‘A’ for scores 90-100​
- ‘B’ for scores 80-89​
- ‘C’ for scores 70-79​
- ‘D’ for scores 60-69​
- ‘F’ for scores below 60​ ​

Steps:​
1. Create a ‘score’ variable and ask user to input score​
2. Use ‘if…elif….else’ to assign grades based on the score range.​
3. Print the grade.​

-------------------------------------------------------------------

# Task 5: Validating User Input​
Write a program that asks for the user’s age and validate that it is a positive integer before checking if they are eligible to vote.​

1. Ask the user for their age and store it into the ‘age’ variable​
2. First, check if ‘age’ is less than 0​
- If true, print “Age cannot be negative”​
3. Then, check if age is more than or equals to 18​
- If true, print “Eligible to vote”​
- Else, print “Not eligible to vote”​

-------------------------------------------------------------------

# Task 6: CNY Shopping Spree​
Ryan wants to use his CNY Red Packet money to buy gaming items.​

- If he has $150 or more, he can buy a gaming keyboard.​
- Else if he has $100 or more, he can buy a new game.​
- Else if he has $50 or more, he can buy a gaming mouse.​
- Else if he has $20 or more, he can buy a gaming mouse pad.​
- Else, he can only buy snacks.​ ​

Write a Python program that asks the user for ​
the amount of ang pow money Ryan has and ​
displays what he can buy.​
Your program must have the option to buy at least 5 items.​