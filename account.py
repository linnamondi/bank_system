class Account:
    def __init__(self,name):
        self.name=name
        self.deposits=[]
        self.withdrawals=[]
        self.statement=[]
        self.balance=0
        self.loan=0
        self.frozen=False



    def deposit(self,amount):
        if self.frozen:
            return "Account is frozen"
        if amount>0:
            self.deposits.append[amount]
            self.statement.append(f"deposited {amount} and your balance is {self.balance}")
        else:
            return f"deposit must be greater then zero"
    def withdrawal(self,amount):
        if amount>self.balance:
            return f"insufficient balance"
        elif amount<0:
            return f"the amount must be greater than zero"
        else:
            self.withdrawals.append[amount]
            self.statement.append (f" withdrew: {amount}")
    def transfer(self,amount,other_account):
        if amount<=0:
            return"amount must be greater than zero"
        elif amount>self.get_balance():
            return "insufficient balance for transfer"
        else:
            self.withdrawals.append(amount)
            other_account.deposit(amount)
            self.statement.append(f"Transfered ${amount} to {other_account.name}")
    def get_balance(self):
        total_deposits=sum(self.deposits)
        total_withdrawals=sum(self.withdrawals)
        return total_deposits-total_withdrawals
    def requestloan(self,amount):
        if amount>0:

            self.loan+=amount
            self.deposits.append(amount)
            self.statement.append(f"Loan requested :${amount}")
        else:
            return "Loan amount must be greater than zero"
    def repay_Loan(self,amount):
        if amount<0:
            return "repayment amount must be greater than zero"
        elif amount>self.get_balance():
            return"insufficient amount to repay the loan "
        elif amount>self.loan:
            extra=amount-self.loan
            self.loan=0
            self.widthrawals.append(amount)
            self
        else:
            self.loan -=amount
            self.withdrawals.append(amount)
            self.statement.append(f"loan repaid ${amount}")
    def view_details(self):
        return f"owner:{self.name},balance:{self.get_balance()}{self.loan}"
    def generate_statement(self):

        print(f" this is a  Statement for {self.name}")
        for amount in self.deposits:
            print(f"Deposit: {amount}")
        for amount in self.withdrawals:
            print(f"Withdrawal: {amount}")
        print(f"Loan: {self.loan}")
        print(f"Balance: {self.get_balance()}")
    def freeze_account(self):
        self.frozen = True
        return " your Account has been frozen"
    def unfreeze_account(self):
        self.frozen = False
        return " Your Account has been unfrozen"
    
    def close_account(self):
        self.deposits.clear()
        self.withdrawals.clear()
        self.loan = 0
        return "Your Account has been closed"


