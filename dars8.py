
def foydalanuvchi_info(ism, familiya, tugilgan_yil, tugilgan_joy,email,telefon):
    foydalanuvchi = {
        'ism': ism,
        'familiya': familiya,
        'tugilgan_yil': tugilgan_yil,
        'tugilgan_joy': tugilgan_joy
    }
    if email:
        foydalanuvchi['email'] = email
    if telefon:
        foydalanuvchi['telefon'] = telefon

    return foydalanuvchi

ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
tugilgan_yil = input("Tug'ilgan yilingizni kiriting: ")
tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")
email = input("Email manzilingizni kiriting: ")
telefon = input("Telefon raqamingizni kiriting: ")

foydalanuvchi_malumotlari = foydalanuvchi_info(ism, familiya, tugilgan_yil, tugilgan_joy, email, telefon)

print("Foydalanuvchi ma'lumotlari:")
print(foydalanuvchi_malumotlari)


mijozlar =[]
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(foydalanuvchi_malumotlari(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break

print("Mijozlar:")
for foydalanuvchi_mijoz in mijozlar:
    print(f"{foydalanuvchi_mijoz['ism'].title()} {foydalanuvchi_mijoz['familiya'].title()},"
          f"{foydalanuvchi_mijoz['yoshi']} yoshda, telefoni: {foydalanuvchi_mijoz['telefon']}")



def kattasi(x,y,z):
    mx  = x
    if y>=mx:
        mx = y
    if z>=mx:
        mx = z
    return mx
print(kattasi(20,30,-5))



def aylana_r(radius,p=3.14):
    aylana = {"radius":radius,
              "diametr":2*radius,
              "perimetr":2*radius*p,
              "yuza":p*radius**2}
    return aylana

print(aylana_r(15))


def tub_sonlar_t(mn, mx):
    tub_sonlar = []
    for n in range(mn, mx + 1):
        tub = True
        if (n == 1):
            tub = False
        elif (n == 2):
            tub = True
        else:
            for x in range(2, n):
                if (n % x == 0):
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar


print(tub_sonlar_t(1, 100))


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(100))
