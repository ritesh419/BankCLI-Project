import json
import os

from .models import BankAccount, SavingsAccount, CurrentAccount

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
        json.dump(data, f, indent=4)


def load_accounts(filepath="accounts.json"):
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        accounts = {}
        for name, acc_data in data.items():
            if acc_data["type"] == "SavingsAccount":
                acc = SavingsAccount(acc_data["name"], acc_data["balance"])
            else:
                acc = CurrentAccount(acc_data["name"], acc_data["balance"])
            acc.transactions = acc_data["transactions"]
            accounts[name] = acc
        return accounts
    except json.JSONDecodeError:
        return {}