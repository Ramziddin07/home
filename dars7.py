dostlar = {
    'rashid':['termintor','rambo','titanic'],
    'anton':['tenet','inception','inerstellar'],
    'athom':['abdullajon','bomba','shaytanat'],
    'xurshid':['mahallada duv-duv gap','john wick'],

    }

for ism, kinolar in dostlar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for til in kinolar:
        print(til.title())


davlatlar = {
    'uzbekiston':{'poytaxt':'toshkent',
           'hududi':448978,
           'aholisi':33000000,
           'valyuta':'som'
           },
    'rossiya': {'poytaxt': 'moskva',
                   'hududi': 448978,
                   'aholisi': 33000000,
                   'valyuta': 'som'
                   },
     'aqsh':{'poytaxt':'washington',
           'hududi':448978,
           'aholisi':33000000,
           'valyuta':'som'
           },
    'malayziya': {'poytaxt': 'Kuala-Lumpur',
                   'hududi': 448978,
                   'aholisi': 33000000,
                   'valyuta': 'som'
                   },
    }
print(input("Davlat nomoini kiriting"))
for davlat,malumot in davlatlar.items():
    if davlat in davlatlar:
        print(f"\n {davlat.title()}ning poytaxti {malumot['poytaxt'].title()},\n "
             f"{malumot['hududi']} kv.km\n "
             f"Aholisis:{malumot['aholisi']}\n"
             f" Pul birligi:{malumot['valyuta']}")

    else:
        print('malumot yoq')
