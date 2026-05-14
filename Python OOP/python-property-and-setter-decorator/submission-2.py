class BankAccount:
    def __init__(self, balance: int): 
        self.__balance1 = balance # Don't modify this line
    
    @property
    def balance1(self) -> int: # TODO: Convert this method to use the @property decorator
        return self.__balance1
        
    @balance1.setter
    def balance1(self, value: int) -> None: # TODO: Convert this method to use the @property decorator
        if value >= 0:
            self.__balance1 = value
        else:
            print("Balance cannot be negative!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.balance1)
account.balance1 = -100
