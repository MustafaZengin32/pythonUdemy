sozluk={
     'reg':"regresyon modeli",
     'loj':"lojistik regresyon",
     'cart':"classification and reg"     
     };

#add

sozluk['gbm']="gradient boosting mac";#sona eklemek

print(sozluk);

print('********************************************');

#change

sozluk['reg']="coklu dogrusal regresyon";


print(sozluk);

print('********************************************');


sozluk[1]="yapay sinir aglari";#bu sekilde 1 i index degil key olarak algilar ve sona ekler

print(sozluk);

#sozcuklerde key ler sadece sabit veri yapisi ile olusturulur list vb olmaz hata verir
#int string degerler atanabilir ,tuple da sabit oldugu icin atanabilir











