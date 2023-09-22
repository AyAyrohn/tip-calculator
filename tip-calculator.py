print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $")) 
percent = int(input("What percentage tip would you like to give?  12, 15, or 20 "))
members_in_group = int(input("How many people to split the bill? "))

tip_choice = int(percent) / 100 

fair_share = ((total * tip_choice + total) / members_in_group)

rounded_share = round(fair_share, 2)

print(f"Each person should pay: ${rounded_share}")