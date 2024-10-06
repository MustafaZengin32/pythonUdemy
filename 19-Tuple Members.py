t=('ali','veli',1,2,3,[1,1,2,3,4],1);

#elemanlara erisme list gibi

print(t[1]);#veli

print(t[3]);#2

print(t[0:3]);#('ali', 'veli', 1)

#t[2]=99;#TypeError: 'tuple' object does not support item assignment
         #Hata aldik cunku tuple nesnesi degisiklige izin vermez
         

print(t.index('ali'));#0


print(t.count(1));#2








