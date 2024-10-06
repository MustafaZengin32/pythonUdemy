
set1=set([1,3,5]);

set2=set([1,2,3]);

#intersection kesisim &

print(set1.intersection(set2)); #{1, 3}

print(set2.intersection(set1));#{1, 3}

print(set1&set2);#{1, 3}

kesisim=set1&set2;

print(kesisim);#{1, 3}

#union 

print(set1.union(set2));#{1, 2, 3, 5}

bilesim=set1.union(set2);

print(bilesim);#{1, 2, 3, 5}

set1.intersection_update(set2) #bunda kesisimde yer alan ifadeler set1 in elemani olur

print(set1);#{1, 3}

print(set2);


set2.intersection_update(set1) #bundada kesisimde yer alan elemanlar set2 nin elemanlari oldu

print(set1);

print(set2);#{1, 3}













