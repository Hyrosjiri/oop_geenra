from utils import clear_screen
from administrator import Administrator
from customer import Customer
from user import User

def main():
    user = User("Petr", "petr@email.cz", "1234")
    admin = Administrator("Tomáš", "tomas@email.cz", "admin123", 3, 15)
    customer = Customer("Jana", "jana@email.cz", "jana123", 1001, 2500)

    user.print_profil()
    admin.print_profil()
    customer.print_profil()

    admin.remove_user(user)

    customer.add_money(500)
    customer.show_balance()

if __name__ == "__main__":  
    clear_screen()
    main()
    input()