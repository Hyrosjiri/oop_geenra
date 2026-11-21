class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def print_profil(self):
        print(f"Jméno: {self.name}")
        print(f"Email: {self.email}")

    def edit_password(self, new_password):
        self.password = new_password
        return True

    def check_password(self, password):
        if self.password == password:
            return True
        return False