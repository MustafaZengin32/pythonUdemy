#sirasiz kapsayici degistirilebilir
#listeler sirali kapsayici degistirilebilir
#tuple sirali kapsayici degistirilemez
#key value

soz={
     'reg':"regresyon modeli",
     'loj':"lojistik regresyon",
     'cart':"classification and reg"     
     };

print(soz);

print(len(soz));#3

soz1={
     'reg':10,
     'loj':20,
     'cart':30    
     };

print(soz1);


soz2={
     'reg':["rmse",10],
     'loj':["mse",20],
     'cart':["cse",30]    
     };

print(soz2);







