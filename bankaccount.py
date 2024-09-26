
class BankAccount:
    def __init__(self, account_number, balance=0):#Function that starts their account balance at 0.
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):#Function for the users deposit.
        if amount > 0:
            self.balance += amount
            return True#If true add amount
        return False#If false show error message(later)

    def withdraw(self, amount):#Function for the users withdrawal.
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True#If true withdraw amount
        return False#If false show errer message(later)

    def get_balance(self):#Function to obtain the users balance.
        return self.balance

def create_account():#Function for the user to create and account
    account_number = input("Enter account number: ") #Allows the user to input account number.
    initial_balance = float(input("Enter initial balance: "))#Allows the user to input account balance.
    return BankAccount(account_number, initial_balance)#Tells the user the account number and initial balance.

def main():#Function to show the user the menu.
    accounts = {}
    while True: #Shows the menu while it is true.
        print("\n1. Create Account")#Tells the user their options.
        print("2. Deposit")#Tells the user their options.
        print("3. Withdraw")#Tells the user their options.
        print("4. Check Balance")#Tells the user their options.
        print("5. Exit")#Tells the user their options.
        
        choice = input("Enter your choice (1-5): ")#Allows the user to decide what they are doing.
        
        if choice == '1':#If the users choice is 1, create account.
            account = create_account()#Allows the user to create a new account.
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")#Tells the user their account was created succesfully.
        
        elif choice in ['2', '3', '4']:#If the user selects options 2,3, or 4.
            account_number = input("Enter account number: ")#Allows the user to input account number.
            if account_number in accounts: #Checks for if the account number is in the active accounts.
                account = accounts[account_number]
                if choice == '2':#If the user selects 2
                    amount = float(input("Enter deposit amount: "))#Adds their deposit to their balance.
                    if account.deposit(amount):#Checks the amount
                        print(f"Deposited ${amount:.2f} successfully!")#Tells the user it was deposited succesfully.
                    else:#Does this instead
                        print("Invalid deposit amount.")#Tells the user their deposit was invalid.
                elif choice == '3':#Checks if the choice is option 3.
                    amount = float(input("Enter withdrawal amount: "))#Allows the user to withdraw money from their account.
                    if account.withdraw(amount):#Checks if the user selcts withdraw.
                        print(f"Withdrawn ${amount:.2f} successfully!")#Tells the user their money was withdrawn succesfully.
                    else:#Does this instead.
                        print("Invalid withdrawal amount or insufficient funds.")#Tells the user their withdrawal was invalid.
                else:#Does this instead.
                    print(f"Current balance: ${account.get_balance():.2f}")#Tells the user their current balance.
            else:#Does this instead.
                print("Account not found.")#Tells the user their account was not found.
        
        elif choice == '5':#Checks if the user selects option 5.
            print("Thank you for using our banking system. Goodbye!")#Thanks the user.
            break
        
        else:#Checks if the user submits an invalid input.
            print("Invalid choice. Please try again.")#Tells the user their choice was invalid.

if __name__ == "__main__":
    main()
