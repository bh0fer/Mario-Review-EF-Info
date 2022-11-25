
feld =[[2,4,4,4,2],[1244,2,4,2,2],[2,2,4,4,2],[2,4,4,4,4],[4,4,4,4,4]]

#print('hallo', Spielfeld[0][0])
#print(f'hallo      {Spielfeld[0][0]}', )  #formatiert

def spielfeld():
    zeilennummer=1
    print('          A      B      C      D      E')
    for zeile in feld:
        print('      +------+------+------+------+------+')
        print('      |      |      |      |      |      |')
        print(f'   {(zeilennummer)}  ', end='')
        for zelle in zeile:
            if zelle >= 10000:
                print(f'| {(zelle)}', end='')
            elif zelle >= 1000:
                print(f'| {(zelle)} ', end='')
            elif zelle >= 100:
                print(f'|  {(zelle)} ', end='')
            elif zelle >= 10:
                print(f'|  {(zelle)}  ', end='')
            else:
                print(f'|   {(zelle)}  ', end='')
        print('|')
        print('      |      |      |      |      |      |')
    print('      +------+------+------+------+------+')
    zeilennummer= zeilennummer+1
    
def transform_eingabe(raw):
    raw = raw.upper()
    raw = raw.replace(' ','').replace('-','').replace('.','').replace(',','').replace('/','').replace(';','').replace(':','')
    x = raw[0]
    if not x.isalpha():
        print('Kein Buchstabe...')
        return False
    y = raw[1]
    if not y.isnumeric():
        print('Keine Zahl...')
        return False
    return [x, y]

eingabe = input('Wählen sie ein Feld zwischen A,1 und E,5 aus:')

Koordinaten = transform_eingabe(eingabe)
if Koordinaten:
    print('Koordinaten', Koordinaten)
else:
    print('Keine Koordinaten')
