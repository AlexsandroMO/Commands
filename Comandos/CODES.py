import pandas as pd

df = pd.read_excel('Pasta1.xlsx')
df = df.fillna('')

for i in df:
    print(i, end=' | ')

for b in range(0, len(df)):
    print('')
    for a in df:
        print('[{}] - {}'.format(len(str(df[a][b])), df[a][b]), end=' | ')
        
        
 #------------------------------------
columnas = [4,25,20,3]
print('---------------------------------', end='')
for b in range(0, len(df)):
    print('')
    cont = 0
    print('|', end='')
    for a in df:
        print('{}{}'.format(df[a][b],(columnas[cont] - len(str(df[a][b]))) * ' '), end='|')
        cont += 1
