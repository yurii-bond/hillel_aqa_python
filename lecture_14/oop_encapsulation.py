class BankAccount:
    def __init__(self, account_number, entry_balance=0):
        self.__balance = entry_balance
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    @balance.setter
    def balance(self, value):
        if isinstance(value, int):
            self.__balance += value


my_acc = BankAccount(account_number='12345890987654323456', entry_balance=1_000_000)
print(my_acc.account_number)
print(my_acc.balance)

my_acc.balance = 2_000_000

# print(my_acc.__balance)
print(my_acc.balance)
