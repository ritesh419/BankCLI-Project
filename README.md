Here is a complete, well-structured `README.md` file tailored specifically for your Python banking application. You can copy and paste this directly into your GitHub repository.

***

```markdown
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

## 🚀 How to Run

### Prerequisites
* Python 3.x installed on your machine. No external libraries are required.

### Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/pybank.git](https://github.com/yourusername/pybank.git)
   ```
2. Navigate to the project directory:
   ```bash
   cd pybank
   ```
3. Run the script:
   ```bash
   python main.py 
   ```
   *(Note: Replace `main.py` with the actual filename of your Python script)*

---

## 💻 Usage Preview

When you run the script, you will be greeted with the main menu:

```text
─── PyBank ───────────────────
1. Create account
2. Deposit
3. Withdraw
4. Show balance & history
5. Exit
──────────────────────────────
Enter your choice between [1-5]: 
```

**Example Workflow:**
1. Select `1` to create an account.
2. Choose between a Savings (`1`) or Current (`2`) account.
3. Enter your name to register.
4. Use the menu to deposit funds, withdraw, or check your balance and complete transaction history!

---

## 📂 Project Structure

* **Core Classes:**
  * `BankAccount`: The base class managing balances, names, and general transactions.
  * `SavingsAccount`: Adds a 4% default interest rate and withdrawal fees.
  * `CurrentAccount`: Adds overdraft functionality.
* **Exceptions:**
  * `BankError`: Base exception for application-specific errors.
  * `InsufficientFundsError`: Triggered when withdrawal exceeds balance/overdraft.
  * `InvalidAmountError`: Triggered on negative or zero amounts.
* **Helper Functions:** Clean, separated logic for CLI inputs (`create_account`, `deposit`, `withdraw`, `show_balance`).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/pybank/issues) if you want to contribute.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
```
