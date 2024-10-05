notlar=[90,80,70,50];


liste1=['b',33,notlar];

print(type(liste1[2]));#<class 'list'>

print(type(liste1[1]));#<class 'int'>

print(liste1[0]);#b

print(liste1[1]);#33

print(liste1[2]);#[90, 80, 70, 50]

tum_liste=[notlar,liste1];

print(tum_liste);#[[90, 80, 70, 50], ['b', 33, [90, 80, 70, 50]]]

del tum_liste;

#print(tum_liste);#hata verir cunku silinmisti







