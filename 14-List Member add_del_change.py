liste=['ali','veli','berkcan','ayse'];

print(liste);

#veli yerine velinin babasi yazdir

liste[1]='velinin_babasi';

print(liste);

#change

liste[1]='veli';

liste[0:3]='alinin_babasi','velinin_babasi','berkcanin_babasi';

print(liste);#['alinin_babasi', 'velinin_babasi', 'berkcanin_babasi', 'ayse']

#add

liste=liste+['kemal'];

print(liste);#['alinin_babasi', 'velinin_babasi', 'berkcanin_babasi', 'ayse', 'kemal']

#del

del liste[2];#Liste nin 2.index i yani 3.elemani 'berkcanin_babasi' sini siler

print(liste);#['alinin_babasi', 'velinin_babasi', 'ayse', 'kemal']




















            
            