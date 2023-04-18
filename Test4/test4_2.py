class Account:
    def __init__(self, account_number, first_name, last_name, balance, interest_rate):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.interest_rate = interest_rate
        
    def get_account_number(self):
        return self.account_number   
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name
    def get_balance(self):
        return self.balance
        
    def get_interest_rate(self):
        return self.interest_rate
        
    def get_interest(self):
        return self.interest_rate * self.balance
        
    def print_account(self):
        account = self.account_number , " " , self.first_name , " " , self.last_name , " " , self.balance , " " , self.interest_rate
        print (account)
        



accounts = []
accounts.append(Account(1001, 'Bruce', 'Lee', 24532.13, 0.05))
accounts.append(Account(1002, 'Liu', 'Yifei', 32393.96, 0.06))
accounts.append(Account(1003, 'Gal', 'Godot', 30232.22, 0.075))
accounts.append(Account(1337, 'Conner','Osborn',999.99,99.99))
total = 0
for account in accounts:
    total += account.get_balance()
    account.print_account()
print("Total balance: {}".format(total))

#Figured it out :D