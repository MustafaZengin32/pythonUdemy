l=["gelecegi","yazanlar"];

s=set(l);

print(s);#{'gelecegi', 'yazanlar'}

print("********************************");

print(dir(s));

print("********************************");

s.add('ile');

print(s);#{'ile', 'gelecegi', 'yazanlar'}

print("********************************");

s.add('gelecegi_git');

print(s);#{'ile', 'gelecegi', 'gelecegi_git', 'yazanlar'}  #sirasiz

print("********************************");

s.add('ile');

print(s);#{'ile', 'gelecegi', 'gelecegi_git', 'yazanlar'} #tekrarsiz unique

print("********************************");

s.remove('ile');

print(s);#{'gelecegi', 'gelecegi_git', 'yazanlar'}

print("********************************");

#s.remove('git');#KeyError: 'git' #git olmadigi icin hata verir

s.discard('ali');#bu sekilde hata vermez , varsa siler yoksa sorun olmaz zaten 

print(s.discard('ali'));

print(s.remove('gelecegi'));

print(s);#{'gelecegi_git', 'yazanlar'}




















