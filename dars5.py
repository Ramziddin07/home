
yangi_cars =['toyota','mazda','hyundai','gm','kia']
for avto in yangi_cars:
    if avto !='gm':
        print(avto.title())
    else:
        print(avto.upper())

login = input('ismingiz nima\n')
if login.lower()!='admin':
    print(f"{login.title()} Xush kelibsiz")
else:
    print("Admin faydalanuvchilar royxatini korasizmi?")


sonlar = float(input("Istalgan sonni kiriting"))
if sonlar > 0:
    print("musbat son")
elif sonlar < 0:
    print("manfiy son")


sonlar = int(input("Istalgan sonni kiriting\n"))
if sonlar > 0:
    print(f"{sonlar**2} ")
elif sonlar < 0:
    print("musbat son kiriting")


yosh = int(input("Yoshingiz neccida"))
if yosh <=4:
    price =0
elif yosh <=18:
    price =10000
elif yosh <=60:
    price =20000
else:
    price = 0
print(f"kirish{price}")