import time as time

class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.__balance = initial_balance
        self.created_at = time.time()

    def __str__(self):
        return f"BankAccount(name={self.name}, balance={self.__balance}, created_at={self.created_at})"

    def __eq__(self, value):
        if isinstance(value, BankAccount):
            return self.name == value.name and self.__balance == value.__balance
        
    def __len__(self):
        return int(time.time() - self.created_at)
    
    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(f"{self.name} & {other.name}", self.__balance + other.__balance)
        return NotImplemented

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError("Balance cannot be negative")