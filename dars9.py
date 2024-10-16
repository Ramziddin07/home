def kopaytma(*sonlar):
    if len(sonlar) == 0:
        return 0
    yigindi = 1
    for son in sonlar:
        yigindi *= son
    return yigindi

sonlar1 = -7, 7, 77


print("yigindi", kopaytma(*sonlar1))

# 2
def kvadratlar(son1, son2, son3, *qolgan_sonlar):
    kvadratlar_royhati = [son1**2, son2**2, son3**2]

    for son in qolgan_sonlar:
        kvadratlar_royhati.append(son**2)

    return kvadratlar_royhati


result = kvadratlar(9, 3, 3, 4, 5, 6)
print(result)

# 3


def talaba_malumotlari(ism, familiya, **malumotlar):
    talaba = {
        'ism': ism,
        'familiya': familiya
    }
    talaba.update(malumotlar)
    return talaba

talaba1 = talaba_malumotlari('Usman', 'Abdullayev', yosh=19, universitet='TATU')
talaba2 = talaba_malumotlari('Ramziddin', 'Bekjonov', yosh=19, universitet='TATU', yoqtirgan_fani='Infarmatika')

print("Talaba 1 ma'lumotlari:", talaba1)
print("Talaba 2 ma'lumotlari:", talaba2)
