liste=['ali','veli','isik'];

print(liste);#['ali', 'veli', 'isik']

#index e gore eleman eklemek insert methodu ile
#insert edilen eleman digerlerinin arasina girer herhangi silme vb olmaz akis sirali devam eder

liste.insert(0,'ayse');

print(liste);#['ayse', 'ali', 'veli', 'isik']#ayse 0 a eklendi ali yi kaydirdi ali simdi 1 de

liste[1]='musti'

print(liste);#['ayse', 'musti', 'veli', 'isik'] #burada ali yerine musti yazdi

liste.insert(2,'nihan');

print(liste);#['ayse', 'musti', 'nihan', 'veli', 'isik'] buda nihan i 2 ye ekledi veli yi kaydirdi

liste.insert(len(liste), 'beren');

print(liste);#['ayse', 'musti', 'nihan', 'veli', 'isik', 'beren'] beren i en son a ekledi

#eleaman silme islemi pop methodu ile

liste.pop(1);

print(liste);#['ayse', 'nihan', 'veli', 'isik', 'beren'] musti yi sildi


