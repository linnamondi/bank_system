from datetime import datetime

class Transaction:
    def __init__(self, amount, narration, transaction_type):
        self.date_time = datetime.now()
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type 
    def __str__(self):
        return f"{self.date_time.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type.title():<10} | ${self.amount:<8.2f} | {self.narration}"


class Account:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.__account_number = account_number
        self.__balance = 0
        self.__loan = 0
        self.__frozen = False
        self.transactions = []

    def deposit(self, amount):
        if self.__frozen:
            return "Account is frozen"
        if amount <= 0:
            return "Deposit amount must be greater than zero"
        self.__balance += amount
        self.__record_transaction(amount, "deposit", "Deposit made")
        return f"Deposited ${amount}. New balance: ${self.__balance}"

    def withdraw(self, amount):
        if self.__frozen:
            return "Account is frozen"
        if amount <= 0:
            return "Withdrawal amount must be greater than zero"
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        self.__record_transaction(amount, "withdrawal", "Withdrawal made")
        return f"Withdrew ${amount}. New balance: ${self.__balance}"

    def transfer(self, amount, other_account):
        if self.__frozen:
            return "Account is frozen"
        if amount <= 0:
            return "Transfer amount must be greater than zero"
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        other_account._Account__balance += amount 
        self.__record_transaction(amount, "transfer", f"Transferred to {other_account.name}")
        other_account.transactions.append(Transaction(amount, f"Received from {self.account_holder}", "transfer"))
        return f"Transferred ${amount} to {other_account.name}"

    def request_loan(self, amount):
        if amount <= 0:
            return "Loan amount must be greater than zero"
        self.__loan += amount
        self.__balance += amount
        self.__record_transaction(amount, "loan", "Loan granted")
        return f"Loan of ${amount} granted. New balance: ${self.__balance}"

    def repay_loan(self, amount):
        if amount <= 0:
            return "Repayment must be greater than zero"
        if amount > self.__balance:
            return "Insufficient funds to repay loan"
        repay_amount = min(amount, self.__loan)
        self.__balance -= repay_amount
        self.__loan -= repay_amount
        self.__record_transaction(repay_amount, "repayment", "Loan repayment")
        return f"Loan repaid: ${repay_amount}. Remaining loan: ${self.__loan}"

    def freeze_account(self):
        self.__frozen = True
        return "Account has been frozen"

    def unfreeze_account(self):
        self.__frozen = False
        return "Account has been unfrozen"

    def close_account(self):
        self.__balance = 0
        self.__loan = 0
        self.transactions.clear()
        return "Account has been closed"

    def generate_statement(self):
        print(f"\nStatement for {self.account_holder} (Account #{self.__account_number})")
        for text in self.transactions:
            print(txt)
        print(f"Balance: ${self.__balance:.2f} | Loan: ${self.__loan:.2f}")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_loan_balance(self):
        return self.__loan

    def is_frozen(self):
        return self.__frozen


    def __record_transaction(self, amount, transaction_type, narration):
        self.transactions.append(Transaction(amount, narration, transaction_type))