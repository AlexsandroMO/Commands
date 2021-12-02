import pandas as pd
import numpy as np

df = pd.read_excel('Pasta1.xlsx')
df = df.fillna('')
#------------------------
num_col = len(df.columns)
col_num = np.arange(num_col)
for i in range(0,len(col_num)):
    col_num[i] = 0

#------------------------
for b in range(0, len(df)): #Count lenght Column
    cont = 0
    for a in df.columns:
        if len(str(a)) > col_num[cont]:
            col_num[cont] = len(a)
        cont += 1

for b in range(0, len(df)): #Count lenght Line
    cont = 0
    for a in df:
        if len(str(df[a][b])) > col_num[cont]:
            col_num[cont] = len(str(df[a][b]))
        cont += 1
#------------------------
print('-' * (col_num.sum() + 5))
print('|', end='')

cont = 0

for i in df.columns:
    print('', end ='')
    print('{}{}'.format(i,(col_num[cont] - len(i)) * ' '), end='|')
    cont += 1

print('\n',end='')
print('-' * (col_num.sum() + 5))
#------------------------

for b in range(0, len(df)):
    print('')
    cont = 0
    print('|', end='')
    for a in df:
        print('{}{}'.format(df[a][b],(col_num[cont] - len(str(df[a][b]))) * ' '), end='|')
        cont += 1

print('\n', end='')
print('-' * (col_num.sum() + 5))
