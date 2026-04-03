# PyBank 🏦

A simple, interactive command-line banking application written in Python. 

This project simulates a basic banking system where users can create different types of accounts, perform transactions, and view their history. It serves as an excellent demonstration of core **Object-Oriented Programming (OOP)** principles in Python, including inheritance, polymorphism, and custom exception handling.

---

## 🌟 Features

* **Multiple Account Types:**
  * **Savings Account:** Accrues interest and charges a $10 fee for withdrawals.
  * **Current Account:** Includes a built-in overdraft limit of $5,000.
* **Transaction Management:** Deposit and withdraw funds safely.
* **Transaction History:** Tracks and logs all account activities automatically.
* **Robust Error Handling:** Utilizes custom exceptions to prevent invalid operations (e.g., negative deposits, insufficient funds, invalid inputs).
* **Interactive CLI:** A user-friendly, loop-based terminal menu.

---

## 🛠️ Concepts Demonstrated

This project is built using standard Python and highlights several foundational programming concepts:

* **Classes & Objects:** Encapsulation of bank account data.
* **Inheritance:** `SavingsAccount` and `CurrentAccount` inherit core behaviors from the base `BankAccount` class.
* **Method Overriding:** Specialized `withdraw()` behaviors for different account types.
* **Custom Exceptions:** `BankError`, `InsufficientFundsError`, and `InvalidAmountError` for precise error catching.
* **Class & Static Methods:** Using `@classmethod` for tracking total accounts and `@staticmethod` for input validation.

---
