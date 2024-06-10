
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Guli']

takrorlanish_soni = 0
for ism in ismlar:
    takrorlanish_soni += 1
    print(f"{ism}, sizga xabarim bor!")

print(f"Kod {takrorlanish_soni} marta takrorlandi")

toq_sonlar = [son for son in range(11, 100, 2)]

for son in toq_sonlar:
    print(son**3)

print("Iltimos, 3 ta eng sevimli kinolaringizni kiriting:")

kinolar = []
for i in range(3):
    kino = input(f"{i+1}-kino nomini kiriting: ")
    kinolar.append(kino)

print("Sizning sevimli kinolaringiz ro'yxati:")
for kino in kinolar:
    print(kino)
