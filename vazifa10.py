class User:
    def __init__(self, ism, familiya, email,adress):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.adress = adress

    def get_info(self):
       return f"{self.ism} {self.familiya}. {self.email} {self.adress} "\

nomzot1 = User('Ismi:'"Ramziddin", "Bekjonov", 'email:'"ramziddinbekjonov@gmail.com" ,'Manzil:'"Xorazm"'da tugilgan')
print(nomzot1.get_info())
