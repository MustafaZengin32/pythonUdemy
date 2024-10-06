sozluk={
     'reg':"regresyon modeli",
     'loj':"lojistik regresyon",
     'cart':"classification and reg"     
     };


#sozluk[0];#KeyError: 0 #sozlukler sirasizdir bu sebeple index ile ulasilamaz

print(sozluk['reg']);


sozluk1={
     'reg':{'reg':"regresyon modeli",
            'loj':"lojistik regresyon",
            'cart':"classification and reg"
            },
     'loj':{'reg':10,
            'loj':20,
            'cart':30
            },
     'cart':"classification and reg"     
     };

print(sozluk1);

print('*******************************************')

print(sozluk1['reg']);

print(sozluk1['loj']['loj']);#20



