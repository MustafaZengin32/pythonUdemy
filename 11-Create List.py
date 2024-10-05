#Veri Yapilari

#Listeler

'''
Degistirilebilir
Farkli Tipte verileri tutabilir
Siralidir

'''

notlar=[90,80,70,50];#Liste tipinde bir obje

print(notlar);#[90, 80, 70, 50]

print(type(notlar));#<class 'list'>

liste=['a',19.3,90];

print(liste);#['a', 19.3, 90]

liste1=['b',33,notlar];

print(liste1);#['b', 33, [90, 80, 70, 50]] #Bu sekilde list icinde list de tanimlanabilir

print(len(liste1));#3


