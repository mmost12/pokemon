from evo.models import Pokemon

f = open('Pokemon.csv', 'r')

for line in f:
    line = line.split(',')
    p = Pokemon()
    p.no =      int(line[0])
    p.name =        line[1]
    p.type1 =       line[2]
    p.type2 =       line[3]
    p.total =   int(line[4])
    p.hp =      int(line[5])
    p.attack =  int(line[6])
    p.defense = int(line[7])
    p.spatk =   int(line[8])
    p.spdef =   int(line[9])
    p.speed =   int(line[10])
    p.save()

f.close()
