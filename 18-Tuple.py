#tuple veri yapisi
#listeler kapsayici sirali ve degistirilebilir
#tuple kapsayici sirali ama list e den farki ise degistirilemez

t=('ali','veli',1,2,3.2,[1,2,3,4]);#('ali', 'veli', 1, 2, 3.2, [1, 2, 3, 4])

print(t);#

print(len(t));#

u='ali','veli',1,2,3.2,[1,2,3,4];

print(u);#tuple () olmadan da olusturulabilir


v=('eleman');

print(type(v));#<class 'str'> #tek elemanli tuple olustururken sonuna virgul konmali yoksa karisir
           
y=('eleman',);

print(type(y));#<class 'tuple'>






