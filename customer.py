from user import User


class Customer(User):
    def __init__(self, name, email, password, account_number, balance=0):
        super().__init__(name, email, password)
        self.account_number = account_number
        self.balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def print_profil(self):
        super().print_profil()
        print(f"Číslo účtu: {self.account_number}")
        print(f"Zůstatek: {self.balance} Kč")

    def show_balance(self):
        print(f"Aktuální zůstatek: {self.balance} Kč")