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
