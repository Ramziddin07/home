class Shaxs:
    def __init__(self, ismi, familiyasi):
        self.ismi = ismi
        self.familiyasi = familiyasi

    def get_info(self):
        return f"{self.ismi} {self.familiyasi}"

class Professor(Shaxs):
    def __init__(self, ismi, familiyasi, fakultet):
        super().__init__(ismi, familiyasi)
        self.fakultet = fakultet

    def get_info(self):
        return f"Professor: {super().get_info()}, Fakultet: {self.fakultet}"

class Foydalanuvchi(Shaxs):
    def __init__(self, ismi, familiyasi, email):
        super().__init__(ismi, familiyasi)
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi: {super().get_info()}, Email: {self.email}"

class Admin(Foydalanuvchi):
    def __init__(self, ismi, familiyasi, email):
        super().__init__(ismi, familiyasi, email)

    def ban_user(self):
        print("Foydalanuvchi bloklandi")

    def get_info(self):
        return f"Admin: {super().get_info()}"


class Talaba:
    def __init__(self, ismi, familiyasi):
        self.ismi = ismi
        self.familiyasi = familiyasi
        self.fanlar = []


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi


admin1 = Admin("Ramziddin", "Bekjonov", "ramziddinbekjonov@gmail.com")
print(admin1.get_info())
admin1.ban_user()


talaba1 = Talaba("Ali", "Valiyev")
fan1 = Fan("Matem")
fan2 = Fan("Informatika")
