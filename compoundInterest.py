initial_amount=float(input("enter initial amount to be invested:"))
years=int(input("enter period of years:"))
interest_rate=float(input("enter ineterest rate:"))
table_header="{:<10} {:<20} {:<15} {:<20}".format("year","starting_balance","interest","ending_balance")
print(table_header)

starting_balance=initial_amount

for year in range(1,years+1):  #iterate over each year
    interest = starting_balance*interest_rate
    ending_balance=starting_balance+interest
    table_row = "{:<10} {:<20.2f} {:<15.2f} {:<20.2f}".format(year, starting_balance, interest, ending_balance)

    print(table_row)           #results for current year

    starting_balance=ending_balance
    
