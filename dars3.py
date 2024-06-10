sonlar =[2,-11,23,57,7,43]

#amallar bajarish

print(sonlar[3] - sonlar[5])
print(sonlar[2] + sonlar[3])
print(sonlar[0] * sonlar[4])

# qiymat

sonlar[1]=7
sonlar[5]=100
sonlar[3]=77
print(sonlar)


# almashtrsh

sonlar[1], sonlar[5] = sonlar [3], sonlar[2]
print(sonlar)


# shaxslar

t_shaxslar =["Alisher Navoiy","Jaloliddin Manguberdi","Amir Temur","Chingizxon"]
z_shaxslar =["Habib","Ilon Mask","Stiv Jobs","Ranoldo"]

print(f"{t_shaxslar}\n{z_shaxslar}")


# frends

frendis =[]
#append
frendis.append("Bekzod")
frendis.append("Sanjar")
frendis.append("Xurshid")
frendis.append("Sarvar")
frendis.append("Athom")
frendis.append("Aziz")

#remove
frendis.remove("Sanjar")
frendis.remove("Aziz")

#Boshiga o`rtasiga va oxirga ism qoshish

frendis.insert(0,"akbar")

frendis.insert(3,"Qodirali")

frendis.append("Anton")
print(frendis)
mexmonlar=[]

mexmonlar = frendis.pop(3)

mexmonlar2 = frendis.pop(3)
mexmonlar3 = frendis.pop(3)

print("mexmonlar",mexmonlar,mexmonlar2,mexmonlar3)
