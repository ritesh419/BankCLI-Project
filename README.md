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

🛠️ Concepts Demonstrated
This project highlights several essential software engineering principles and Python features:

Separation of Concerns (SoC): Dividing the program into distinct sections so each module addresses a specific functionality.

Python Decorators: Wrapping functions to extend behavior (e.g., automated transaction logging) without modifying the core logic.

File I/O & Data Persistence: Safely writing and reading application state to/from the local disk.

Object-Oriented Programming (OOP): Deep utilization of classes, inheritance, method overriding, and static/class methods.

Custom Exception Handling: Creating granular error states for predictable program execution.

🚀 How to Run
Prerequisites
Python 3.x installed on your machine. No external libraries are required.

Execution
Clone the repository:

Bash
git clone [https://github.com/ritesh419/BankCLI-Project.git](https://github.com/ritesh419/BankCLI-Project.git)
Navigate to the project root directory:

Bash
cd BankCLI-Project
Run the application:

Bash
python main.py 
💻 Usage Preview
Upon running main.py, the system will load any existing account data and present the main menu:

Plaintext
─── PyBank ───────────────────
1. Create account
2. Deposit
3. Withdraw
4. Show balance & history
5. Exit
──────────────────────────────
Enter your choice between [1-5]: 
Workflow Example:

Select 1 to create a new Savings or Current account.

Select 2 or 3 to perform transactions (which will be logged automatically via decorators).

Select 5 to exit. The application will safely save your updated data to disk for your next session!

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.
