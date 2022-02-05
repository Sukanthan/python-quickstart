#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip Calculater:")

totla_bill = float(input("What was the Total Bill:£"))
tip = int(input("What percentage of tip you wanted to give 10%,12%,15%: "))
bill_and_tip = totla_bill * tip 
number_of_friends = int(input("How many of you : "))
bill_share = bill_and_tip / number_of_friends
final_bill = round(bill_share, 2)
print(f"Each person pays:£{final_bill}")
