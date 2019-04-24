pri = input()

if (pri == 'vertebrado'):
    seg = input()
    if (seg == 'ave'):
        tri = input()
        if (tri == 'carnivoro'):
            animal = 'aguia'
        else:
            animal = 'pomba'
    else:
        tri = input()
        if (tri == 'onivoro'):
            animal = 'homem'
        else:
            animal = 'vaca'

else:
    seg = input()
    if (seg == 'inseto'):
        tri = input()
        if (tri == 'hematofago'):
            animal = 'pulga'
        else:
            animal = 'lagarta'
    else:
        tri = input()
        if (tri == 'hematofago'):
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'
print(animal)
