dunyo_davlatlari ={
    'Ozbekiston':'Toshkent',
    'ROSSIYA':'Moskva',
    'ITALIYA':'Rim',
    'QIRGISTON':'Nursulton',
    'QOZOGISTON':'Bishkek',
    'SINGAPUR':'Sungapur',
    'MALAYZIYA':'Kuala-Lumpur',
    'AQSH': 'Washington D.C',
    'TOJIKISTON':'Dushanbe',
}
mamlakat = input('Xoxlagan davlatni nomini kiriting.Poytaxtini chiqarib beramiz?:').lower()
poytaxt = dunyo_davlatlari.get(mamlakat.upper())
if poytaxt==None:
    print('Malumot yoq')
else:
    print(f"{mamlakat.title()}ning poytaxti {mamlakat.title()} shahri")

taomlar_royxati = {
        'pitsa': 20000,
        "kola": 7000,
        'non': 4000,
        'choy': 5000,
        'hod dog': 12000,
        'kartoshka free': 16000,
        'tabaka': 15000,
        'polov': 25000
    }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
        buyurtmalar.append(input(f"{n + 1}-taom:"))

for buyurtma in buyurtmalar:
        if buyurtma in taomlar_royxati:
            print(f"{buyurtma.title()} {taomlar_royxati[buyurtma]} so'm")
        else:
            print(f"Kechirasiz, bizda {buyurtma} yoq.")