class account:
    def __init__(self, account_number, balance, account_holder):
        self.__account_number =account_number
        self.__balance = balance
        self.__account_holder =account_holder
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return "watch purchased"
        return "insufficient balance"
    def check_balance(self):
        return self.__balance
mon_compt = account("acc001", 100, "aya")
mon_compt.deposit(500)  
print(mon_compt.withdraw(300))          
