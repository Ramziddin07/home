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
