# variables in python - int, float, string, boolean
# comments in python - single line(#) and multi-line("""", ''')
"""Write a Python program that can do the following:
- You have $50
- You buy an item that is $15, that has a 3% tax
- Using the print()  Print how much money you have left, after purchasing the item.
"""
initial_money = 50
item_price = 15
tax_rate = 0.03
tax_amount = item_price * tax_rate
total_cost = item_price + tax_amount
money_left = initial_money - total_cost
print("Money left after purchasing the item: $", round(money_left, 2))
# string formatting
print("Hi, you have ${:.2f} left after buying the item.".format(money_left))
print(f"Money left after purchasing the item: ${money_left:.2f}")
# getting user input
days_before_birthday = int(input("How many days before your birthday? "))
print(f"Approx. weeks until your birthday: {days_before_birthday // 7} weeks")

# booleans and operators in python - ({comparison ops: ==, !=, <, >, <=, >=}, {logical ops: and, or, not})
# if else statements in python - if, elif, else
# loops in python - for, while
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
x = 0
while x < 3:
    x += 1
    for i in my_list:
        if i == "Monday":
            continue
        print(i)
# functions in python - def, return
# modules in python - import, from ... import
# standard libraries in python - os, sys, math, random, datetime