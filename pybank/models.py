from functools import wraps
from .exceptions import BankError, InsufficientFundsError, InvalidAmountError

def log_transaction(org_func):
    @wraps(org_func)
    def wrapper(self, amount, *args,**kwargs):
        print(f"→ [{org_func.__name__}] {self.name} | amount: {amount}")
        result = org_func(self, amount, *args,**kwargs)
        print(f"→ [{org_func.__name__}] done | new balance: {self.balance}") # ✓ [deposit] done | new balance: 1500
        return result
    return wrapper

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

    @log_transaction
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

    @log_transaction
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

    @log_transaction
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError(amount)
            if amount > (self.balance + self.overdraft_limit):
                raise InsufficientFundsError(amount, self.balance)
        except (InvalidAmountError, InsufficientFundsError):
            raise
        self.balance = self.balance - amount
