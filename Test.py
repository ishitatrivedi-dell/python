class Bank_Account: 
    account_number = 9865321478  # Class variable to keep track of account numbers
    def __init__(self, name, deposit):
        self.name = name
        self.deposit_amount = deposit
        self.user_account_number = Bank_Account.account_number + 1  # Assign the current account number to the user

user1 = Bank_Account("John Doe", 1000)  

print(user1.name)  # Output: John Doe
print(user1.deposit_amount)  # Output: 1000
print(user1.user_account_number)  # Output: 9865321479