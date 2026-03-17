class Bank():
    def __init__(self, balance: int) -> None:
        self.__balance = balance
    def deposit(self, amount_to_deposit: int) -> int:
        if (amount_to_deposit <= 0):
            print("Invalid amount, try again!")
            return
        print(f"You've deposited ${amount_to_deposit:.2f}")
        self.__balance = self.__balance + amount_to_deposit
        return (self.__balance)
    def withdraw(self, amount_to_withdraw: int) -> bool:
        if (amount_to_withdraw <= 0):
                print("Invalid amount, try again!")
                return (False)
        elif (amount_to_withdraw > self.__balance):
                print(f"You tried to withdraw ${amount_to_withdraw:.2f}\nYou don't have this amount.")
                return (False)
        else:
             self.__balance = self.__balance - amount_to_withdraw
        print(f"You've withdrawn {amount_to_withdraw}")
        return (True)
    def get_balance(self) -> int:
        print(f"Your balance is ${self.__balance:.2f}")
        return self.__balance
if __name__ == "__main__":
     account1 = Bank(-1)
     account1.get_balance()
     account1.withdraw(15)
     account1.deposit(50)
     account1.withdraw(55)
     account1.get_balance()
