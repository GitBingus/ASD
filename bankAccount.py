class BankAccount:
    def __init__(self, pinnumber):
        self.pinnumber = pinnumber
        self.balance = 100

    def deposit(self, pinnumber, amount):
        if pinnumber == self.pinnumber:
            self.balance += amount
            return self.balance
        else:
            return "Invalid PIN"

    def withdraw(self, pinnumber, amount):
        if pinnumber == self.pinnumber:
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                return "Insufficient funds"
        else:
            return "Invalid PIN"

    def get_balance(self, pinnumber):
        if pinnumber == self.pinnumber:
            return self.balance
        else:
            return "Invalid PIN"

    def change_pin(self, oldpinnumber, newpinnumber):
        if oldpinnumber == self.pinnumber:
            self.pinnumber = newpinnumber
            return "PIN changed successfully"
        else:
            return "Invalid PIN"