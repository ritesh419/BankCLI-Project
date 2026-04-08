# ──all main classes────────────────────────────────

import json
import os


class BankAccount:
    bank_name = "SBI"
    bank_branch = "Khatima"
    total_accounts = 0

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []
        BankAccount.total_accounts += 1

    def __str__(self):
        return f"Name: {self.name} - Balance: {self.balance}"

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance = self.balance - amount
        self.transactions.append(f"Withdraw: {amount}")

    def get_history(self):
        return f"{self.transactions}"

    @classmethod
    def get_total(cls):
        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


class SavingsAccount(BankAccount):
    FEE = 10

    def __init__(self, name, balance=0, interest_rate=1.04):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance = self.balance * self.interest_rate

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError(amount)
        except InvalidAmountError:
            raise
        total = amount + self.FEE
        super().withdraw(total)
        print(f"Fee of {self.FEE} charged")


class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=5000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError(amount)
            if amount > (self.balance + self.overdraft_limit):
                raise InsufficientFundsError(amount, self.balance)
        except (InvalidAmountError, InsufficientFundsError):
            raise
        self.balance = self.balance - amount


# ── all exception classes────────────────────────────────────


class BankError(Exception):
    pass


class InsufficientFundsError(BankError):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")


class InvalidAmountError(BankError):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Amount = {amount} :Input amount can only be greater than 0")


# ── helper functions ─────────────────────────────────────


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
    user = accounts[owner].deposit(amount)
    # print(accounts[owner])
    print(user)
    return user


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


def account_to_dict(accounts):
    return {
        "type": type(accounts).__name__,
        "name": accounts.name,
        "balance": accounts.balance,
        "transactions": accounts.transactions,
    }


def save_accounts(accounts, filepath="accounts.json"):
    data = {name: account_to_dict(acc) for name, acc in accounts.items()}
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def load_accounts(filepath="accounts.json"):
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        accounts = {}
        for name, acc_data in data.items():
            if acc_data["type"] == "SavingAccount":
                acc = SavingsAccount(acc_data["name"], acc_data["balance"])
            else:
                acc = CurrentAccount(acc_data["name"], acc_data["balance"])
            acc.transactions = acc_data["transactions"]
            accounts[name] = acc
    except json.JSONDecodeError:
        return {}


# ── main menu loop ───────────────────────────────────────────────────

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
