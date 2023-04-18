years = float(input("Enter the number of years to simulate: "))
months = int(12 * years)
annual_interest_rate = float(input("Enter the annual interest rate: "))
monthly_interest_rate = annual_interest_rate / 12.0
monthly_deposit = float(input("Enter the monthly amount deposited: "))
balance = 0.0
month_count = 0
month = 1
interest = 0
print('Month ', 'Interest ','Current Balance ')

while months >= 0:
   interest = monthly_interest_rate * balance 
   balance = balance + monthly_deposit
   balance = balance + interest
   print(month, interest,  balance)
   month = month + 1
   months = months - 1
  
    

