kocha="Al-Xorazmiy"
mahalla="Tinchlik"
tuman="Urganch"
viloyat="Xorazm"
print(kocha,'kochasi,' + mahalla, 'mahallasi,'+ tuman, 'tumani,'+ viloyat,'viloyati')

kocha=input('Ko`chaning kiriting:')
mahalla=input('Mahallani kiriting:')
tuman=input('Tumanni kiriting:')
viloyat=input('Viloyatni kiriting:')
print( kocha," ko`chasi," + mahalla, ' mahallasi,'+tuman,'tumani,' + viloyat,'viloyati.' )

kocha=input('Ko`chaning kiriting:')
mahalla=input('Mahallani kiriting:')
tuman=input('Tumanni kiriting:')
viloyat=input('Viloyatni kiriting:')
print( kocha," ko`chasi," + '\n' + mahalla, ' mahallasi,'+'\n'+tuman,'tumani,'+ '\n' + viloyat,'viloyati.' )

kocha=input('Ko`chaning kiriting:')
mahalla=input('Mahallani kiriting:')
tuman=input('Tumanni kiriting:')
viloyat=input('Viloyatni kiriting:')
manzil=kocha + mahalla + tuman + viloyat
print( f"Manzil {manzil} ")

kocha=input('Ko`chaning kiriting:')
mahalla=input('Mahallani kiriting:')
tuman=input('Tumanni kiriting:')
viloyat=input('Viloyatni kiriting:')
manzil=kocha + mahalla + tuman + viloyat
print( manzil.title())
print( manzil.upper())
print( manzil.lower())
print( manzil.capitalize())

a=input("Yoshingizni kiriting:")
b=2024-int(a)
print("Yilingiz:" + str(b))

a=input("1-sonni kiriting:")
b=input("2-sonni kiriting:")
x=int(a)+int(b)
y=int(a)-int(b)
z=int(a)*int(b)
d=int(a)/int(b)
print("Yig`indisi:" +str(x),'\nKo`paytmasi:' + str(y),"\nAyirmasi:" + str(z),"\nBo`linmasi:"+ str(d))
