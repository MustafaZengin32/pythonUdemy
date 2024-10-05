liste=[10,20,30,40,50];

print(liste[0]);


#print(liste[6]);

#6. index liste de olmadigi icin yukaridaki hatayi verir

print(liste[0:2]);#[10, 20]


print(liste[:2]);#[10, 20] #bunu 0:2 oalrak algilar 

print(liste[2:]);#[30, 40, 50]#bunu ise 2 den sonuncu elemana kadar diye algilar

yeni_liste=['a',10,[20,30,40,50]];

#print(yeni_liste[3]);#IndexError: list index out of range verir , cunku icindeki list tek eleman

#Mesela icteki list de 30 a ulasalim

print(yeni_liste[2][1]);#30


















            
            