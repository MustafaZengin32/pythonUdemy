#Setler -->Kumeler

#sirasiz essizdir-tekrarsiz degistirilebilir
#hiz essiz istersek kullanilir
#liste  ya da tuple ya da string vb olusturup set icine atilir ve bu sekilde set olusturulur

l=[1,'a','ali',123];

s=set(l);

print(s);#{'ali', 1, 'a', 123}

t=('a','ali');

u=set(t);

print(u);#{'ali', 'a'}

ali="lutfen_ata_bakma_uzaya_git";

v=set(ali);

print(v);#{'_', 'e', 't', 'u', 'k', 'z', 'f', 'n', 'g', 'a', 'b', 'm', 'y', 'l', 'i'}
         #tekrarsiz-unique , sirasiz , degistirilebilir
         
#v[0] # TypeError: 'set' object is not subscriptable   #setler sirasizdir hata verir

     











