liste=['ali','veli','isik','ali','veli'];

#count;

print(liste.count('veli'));#2 #'veli' den liste de kac tane vae onu gosterir

#print(liste.count('i'));#0 verir cunku elaman olarak bakar icerigine bakmaz


#copy;#Listeyi kopyalar ilerde degisikliklerden sonra eski haline bulmak icin

liste_yedek=liste.copy();

print(liste_yedek);#['ali', 'veli', 'isik', 'ali', 'veli']


#extend #iki listeyi birlestirmek icin kullanilir Liste yapisi degisir

liste.extend(['a','b','c']);


print(liste);#['ali', 'veli', 'isik', 'ali', 'veli', 'a', 'b', 'c']

#index #bir elemanin kacinci index de oldugunu getirir

print(liste.index('isik'));#2


print(liste.index('ali'));#0 #ilk index ini verir

#reverse #elemanlarini terse cevirir ters den yazdirir , buda yapiyi degistirir

liste.reverse();

print(liste);#['c', 'b', 'a', 'veli', 'ali', 'isik', 'veli', 'ali']

#sort , siralar

liste.sort();

print(liste);#['a', 'ali', 'ali', 'b', 'c', 'isik', 'veli', 'veli']

#hub=[1,3,'a','b'];

#hub.sort();

#print(hub);#TypeError: '<' not supported between instances of 'str' and 'int' 
            #Farkli veri tipleri oldugu icin siralamada hata verir
            
#clear #liste icindeki elemanlari temizler del ise tamamen listeyi siler

cub=['d','a','b'];


cub.clear();

print(cub);#[]



            
