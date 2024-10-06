'''

difference() methodu her iki kumenin farkini verir


'''

#difference

set1=set([1,3,5]);

set2=set([1,2,3]);

print(set1.difference(set2));#{5} #set1 de olup set2 de olmayanlari verir

print(set2.difference(set1));#{2}

print(set1.symmetric_difference(set2));#{2, 5}

print(set1-set2);#{5} #difference methodunun alternatifi









