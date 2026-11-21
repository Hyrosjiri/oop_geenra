from user import User

class Administrator(User):
    def __init__(self, name, email, password, permission_level, manager_users_count):
        super().__init__(name, email, password)
        self.permission_level = permission_level
        self.manager_users_count = manager_users_count

    def remove_user(self, user):
        print(f"Uživatel {user.name} byl odstraněn.")

    def print_profil(self):
        super().print_profil()
        print(f"Úroveň oprávnění: {self.permission_level}")
        print(f"Počet spravovaných uživatelů: {self.manager_users_count}")