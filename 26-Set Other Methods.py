#set query

set1=set([7,8,9]);

set2=set([5,6,7,8,9,10]);

print(set1.isdisjoint(set2));#false , cunku burada iki kumenin kesisimi bos mu diye sordu degil

print(set1.issubset(set2));#true #ilk kume ikincisinin alt kumesi mi diye sorar 

print(set2.issuperset(set1));#true #set2 set1 i kapsar mi





