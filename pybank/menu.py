from .models import BankAccount, SavingsAccount, CurrentAccount
from .storage import save_accounts, load_accounts
from .exceptions import BankError

def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Enter only integer.") 


def create_account(accounts):
    choice = get_int_input("Enter any choice: 1. Saving     2. Current: \n")

    if choice not in (1, 2):
        raise BankError("Please enter only number 1 or 2.")

    owner = input("Enter owner's name: \n").strip()
    if not owner:
        raise BankError("Name cannot be empty.")
    if owner.isdigit():
        raise BankError("Name should contains letter, not just numbers.")

    if owner in accounts:
        raise BankError(f"Account for '{owner}' already exists.")

    if choice == 1:
        user = SavingsAccount(owner)
    else:
        user = CurrentAccount(owner)
    accounts[owner] = user
    return user
    # print(f"{type(user).__name__} created for {owner}")

def deposit(accounts):
    owner = input("Enter owner's name: \n").strip()
    if owner not in accounts:
        raise BankError(f"No account found for '{owner}'.")
    amount = get_int_input("Enter the deposit amount: \n")
    accounts[owner].deposit(amount)
    print(accounts[owner])


def withdraw(accounts):
    owner = input("Enter owner's name: \n").strip()
    if owner not in accounts:
        raise BankError(f"No account found for '{owner}'.")
    amount = get_int_input("Enter the withdraw amount: \n")
    accounts[owner].withdraw(amount)

def show_balance(accounts):
    owner = input("Enter owner's name: \n").strip()
    if owner not in accounts:
        raise BankError(f"No account found for '{owner}'.")
    acc = accounts[owner]
    print(f"\n--- {acc.name}'s Account ---")
    print(f"Balance: {acc.balance}")
    print(f"History: {acc.get_history()}")

def account_to_dict(accounts):
    return {
        "type": type(accounts).__name__,
        "name": accounts.name,
        "balance": accounts.balance,
        "transactions": accounts.transactions,
    }

def run():
    accounts = load_accounts()

    while True:
        print("\n─── PyBank ───────────────────")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show balance & history")
        print("5. Exit")
        print("──────────────────────────────")
        try:
            user_choice = get_int_input("Enter your choice between [1-5]: \n")
            if user_choice == 1:
                create_account(accounts)
                save_accounts(accounts)
            elif user_choice == 2:
                deposit(accounts)
                save_accounts(accounts)
            elif user_choice == 3:
                withdraw(accounts)
                save_accounts(accounts)
            elif user_choice == 4:
                show_balance(accounts)
            elif user_choice == 5:
                print("Thank you! for using 'PyBank'.")
                break
            else:
                print("Enter only the valid choice.")

        except (BankError, Exception) as e:
            print(f"Error: {e}")
