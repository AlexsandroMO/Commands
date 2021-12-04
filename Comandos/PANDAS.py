#https://www.goconqr.com/
#https://www.onenote.com/classnotebook?omkt=pt-PT


#https://www.w3schools.com/python/pandas/default.asp


#criar excel - to.excel
writer = pd.ExcelWriter('AC_NCR_SEARCHED.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='BY_NCR')
df2.to_excel(writer, sheet_name='BY_IM')
writer.save()

#unicos itens lista e pandas

lista.sort() ou sorted(lista)
df1 =  df_read[df_read['IM'] != '-'].groupby(['NCR','IM']).count()



#encontrar tabelas em um db
def read_sql_btc():
  conn = sqlite3.connect('db.sqlite3')
  sql_datas = f"""
                   SELECT name FROM sqlite_master WHERE type='table'ORDER BY name;
              """
  read_db = pd.read_sql_query(sql_datas, conn)
  conn.close()
  return read_db

##List Codes

#### lista de 
https://www.vooo.pro/insights/guia-para-iniciantes-de-web-scraping-em-python-usando-beautifulsoup/



'''
# int_str_float - tranforma type
# new_df['Valor Empenhado (R$)'].astype('str')
# new_df['Valor Empenhado (R$)'] = new_df['Valor Empenhado (R$)'].str.lower().str.replace(',', '.')
# new_df['Valor Empenhado (R$)'].astype('float') italicized text
'''



=====================

plot = size
plt.rcParams['figure.figsize'] = (8,5)

=================
Read DF

x = []
with open('drive/My Drive/2019/Files_Colab/201904_Despesas.csv', 'r', encoding='latin-1') as f:
  for linha in f.readlines():
    #print(linha)
    x.append(linha.replace('\n', '').split(';')) #linha.replace('\n', '').split(',')
    
header = x[0]
del(x[0])

y = []
for a in x:
  #print(a)
  y.append(a)
  
dfA = pd.DataFrame(data=y)

#Altera dados de colunas (modificar)
df['FirstName'][df.ID == 103] = "Matt"

df.loc[df.ID == 103, ['FirstName', 'LastName']] = 'Matt', 'Jones'
#https://www.it-swarm.dev/pt/python/alterar-um-valor-com-base-em-outro-valor-em-pandas/1041900404/



dfB = dfA[np.arange(0,len(header),1)]

for a in range(len(header)):
  dfB.rename(columns={a:header[a]}, inplace=True)
  
dfB.head(3)

=================
plt.rcParams['figure.figsize'] = (11,7)
matplotlib, aumentar
--------------------------------

#dodificar tesxtos

df['name']= df['name'].replace(['michael','louis'],['karl','lionel'])




#filter filtro por indice

df_new.iloc[[1,239,243]]

df_new.query('CPF != ""') #Query


#### Acrescentar linhas

df.insert(3,"Capital","Unknown")

dados = [  ['CC-100000-00001-11-001','CTE00000001','ABC_TESTES','BB00001',''],
            ['CC-100000-00001-11-001','CTE00000002','ABC_TESTES','BB00001',''],
            ['CC-100000-00001-11-002','CTE00000002','ABC_TESTES','BB00002',''],
        ]
header = ['CC','CTE','TIPO','IM','NOTA']
df = pd.DataFrame(data=dados, columns=header)

df

dados2 = [  ['CC-100000-00001-11-00x','CTE0000000x','ABC_TESTES','BB0000x','']
     
        ]

header2 = ['CC','CTE','TIPO','IM','NOTA']
df2 = pd.DataFrame(data=dados2, columns=header2)
df2

new = df.append(pd.concat([df2]))
new

#### Muda valores de umacoluna

new_df = df['Atrito'].replace(['Yes', 'No'], [0, 1])


#Procv - join
pd.merge(tabela_1, tabela_2[['campo_1', 'campo_2',...,'campo_n']], on=['campo_em_comum_1'], how='left') #Pode usar, right, inner e outer (full)
pd.merge(tabela_1, tabela_2[['campo_1', 'campo_2',...,'campo_n']], left_on=['campo_em_comum_1'], right_on=['campo_em_comum_2'], how='left') #qd tiver campos diferentes nones



#### Mudar uma coluna baseada em outra
==============
conta = 0

for a in New_Bolo['Ingrediente']:
    print(a , '= Posição ', conta)
    if a == 'Ovo': #Palavra procurada
      New_Bolo['Qt2'].iloc[conta] =  new  #novo arguemnto
    conta = conta + 1
    
====================   

Python Comands
--------------------------------
#### Where
cont = 0
for a in df['CTE']:
  test1 = df2[df2['CTE'] == a]
  print(a)
  print(test1['CTE'])
  
  if test1.index != 0:
    print('ok')
    if df2.loc[df2[df2['CTE'] == a].index[0]][1] == a:
      df.set_value(cont, 'RESULT', 'OK')
    else:
      df.set_value(cont, 'RESULT', 'N')
  else:
    print('nnnnnnn')

  cont+= 1
 -------------------------------
 cont = 0

for a in df['CTE']:
  print('A: ', a)
  cc_use = df[df['CTE'] == a]['NOTA']
  for i in cc_use:
    print('USE: ', i)
    cc_use2 = df2[df2['CC'] == i]
    cc_use2 = cc_use2[cc_use2['CTE'] == a]['CTE']
    for z in cc_use2:
      print('Resultado Final: ', z)
      if df2.loc[df2[df2['CTE'] == a].index[0]][1] == a: #Se dataframe 2 tiver o CTE desejado, escreve na celula de RESULT = OK
        df.set_value(cont, 'RESULT', 'OK')
      else:
        df.set_value(cont, 'RESULT', 'N')
        
  cont+= 1
 -------------------------------
 
 ####Localizar texto dentro de uma string
 nome = 'SMB-316199'

for a in dados['Caminho'].head(20):
  print(a)
  if re.search('\\{}\\b'.format(nome), a, re.IGNORECASE):
    print("Ok")
    print(a)



####Contar itens de uma coluna - Groupby - contagem
df_new['STATUS_NCR'].value_counts() #RELATÓRIO DE VALORES POR COLUNA - OPTION1
df_new.groupby('STATUS_NCR').NCR.count() #RELATÓRIO DE VALORES POR COLUNA - OPTION1
df_new.groupby('STATUS_NCR').count() #TABELA DE QUANTIDADES POR COLUNA
df_new.groupby(['STATUS_NCR']).size().reset_index().rename(columns={0:'COUNT'}) #criando uma nova tabela de contagem

-----------------------
####Alterar Index
import pandas as pd 
  
Creating the index 
idx = pd.Index(['Jan', 'Feb', 'Mar', 'Apr', 'May']) 
  
# Print the index 
print(idx) 
 --------------------
 
 
####Ordenar por Coluna
df.sort_values(by='Valor', ascending=True).head() => Crescente

df.sort_values(by='Valor', ascending=False).head() => Descrescente

####Somatório Geral
df.groupby("Aluno").mean()

####Somatório de Itens por coluna
df["Seminario"].value_counts()
 
####Criar arquivo.csv ou xlsl
df.to_csv

####Excluindo Colunas
df.drop('Nova Coluna', axis=1)



####Exluindo Linha Por Index
df.drop([0, 1]) 

####Ordenar por Coluna
df.sort_values(by="Prova")

####Selecionar linhas específicas
df.loc[[0,1,2]]

####Nova coluna
df['Nova'] = np.nan

####Comparar data framesConcatenar Colunas por [emerge] combina - concatena
result = df_app.merge(df_epm, on='CMX')

####Renomear Colunas
data.rename(columns={'gdp':'log(gdp)'}, inplace=True)

####Selecionar Item específico de Coluna Específica
df['Aluno'].loc[3]

####Cortar coluna
df.drop(['coluna1'], axis=1, inplace=True)

####Concatenar colunas
dados = pd.concat([df, sex], axis=1)

####Substituir valores NaN por outro
df.fillna('-')
#ddf = df.dropna()

####Ler só em cima ou só em baixo de um dataframe
df.tail()
df.head()

####transformar colunas em novas colunas 0 ou 1 
newcolum = pd.get_dummies(df['sex'], drop_first=True)

####Verificar tipo de sistema de predição aplicar
sns.pairplot(suicide)

####Concatenar Data Frames
pd.concat([new_df, new_df])
outra
Frame = Frame.append(pandas.DataFrame(data = SomeNewLineOfData), ignore_index=True)

####renumerar index

df.reset_index()

df.index = pd.Index(np.arange(0,len(df2)))

for a in df.index:
  print(a)
  df.rename(index={a:0}, inplace=True)
  
  df.index = pd.Index(np.arange(0,len(df)))
 
##### Contagem Index
df.index.size

#####Descobrir o index
f2[df2['CTE'] == a].index[0]

####Nomear Index Coluna
df.index.names = ['ID']

####renomerar index
df.rename(index={'0':'ID'})

####setar index em uma coluna
dd = df.set_index('Number(Related product lot(s))')

####Concatenar Colunas
pd.concat([n, siecc], axis=1)

####Filtros
Teste_EQ = EQ[EQ['CC de Montagem'] == Nome_CC]

####Alterar valores de uma coluna, baseado em outra
def relaciona(cols): reavaliar...
  Col_qt = cols['Quantity provided(Product)']
  Col_OBS = cols['OBSERVAÇÃO']
 
  if pd.isnull(Col_qt)
    if Col_OBS != '':
      return '1'
    else:
      return Col_qt
  else:
    return Col_qt

LMA['OBSERVAÇÃO'] = LMA[['OBSERVAÇÃO', 'Mass (kg) (Item).1']].apply(relaciona, axis=1)

####pegar pedaços de uma String
for a in LMA['Number(Related product lot(s))']:
  print(len(a))
  print(a)
  print(a[4::])

####Querry
df[(df["Seminario"] > 8.0) & (df["Prova"] > 3)]
df[(df["Aluno"] == "Harry") & (df["Prova"] == 5)]

####Pegar letras da direta ou da esquerda de uma string
df[-3::]
todo dataframe
conta = 0
for local in LMA['Number(Related product lot(s))']:
  LMA['Number(Related product lot(s))'].iloc[conta] = local[4::]
  conta = conta + 1

####Datas
import pandas as pd
df = pd.read_csv('DataFrame.csv', delimiter=";");

df['Data e Hora'] = pd.to_datetime(df['Data e Hora'])
df['Data'] = df['Data e Hora'].dt.strftime('%Y-%m-%d')
df['Hora'] = df['Data e Hora'].dt.strftime('%H:%M:%S')

del df['Data e Hora']
df = df[['Data', 'Hora', 'Consumo(litros)', 'Valor Acumulado']]

print(df)

Append em for
for i in Teste_EQ['Industrial Mark']:
  new_df = LMA_Construction[LMA_Construction['Number(Related product lot(s))'] == '53A' + i]
  #print(new_df)
  df = df.append(pd.concat([new_df]))

df


http://blog.alura.com.br/lidando-com-datas-e-horarios-no-python/
==========================





#Exercícios Pandas Python

import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

PL = pd.read_excel('PL_result_teeWe.csv_B30_1.xlsx')
PL.to_csv('test.csv')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

PL = pd.read_excel('PL_result_teeWe.csv_B30_1.xlsx')

EQ = pd.read_excel('Equipamentos 2018.xlsx', 'IMZ')

Nome_CC = 'CC-200712-47312-11-001'
#Nome_CC = input('CC: ')
SBR = Nome_CC[16:18:]

#CC-000000-30700-11-001
#CC-000000-30700-12-102
#CC-200569-47317-11-004
#CC-200712-47312-11-001

Teste_EQ = EQ[EQ['CC de Montagem'] == Nome_CC]

Teste_EQ.head()

Teste_EQ.describe()

df_Model = PL.head(1)

#Exluindo Linha Por Index
df_Model.drop([0, 0],inplace=True)
df_Model

for i in Teste_EQ['Industrial Mark']:
  new_df = PL[PL['Number(Related product lot(s))'] == 'LPR-' + i]
  #print(new_df)
  df_Model = df_Model.append(pd.concat([new_df]))

df_Model

lm = df_Model[['Number(Related product lot(s))','Industrial marker(Mounted Product)','Number(Mounted Product)','Number(Item)','Quantity provided(Product)','Designation(Mounted Product)','Mass (kg)(Item).1','Number(Item).1','Designation(Item).1']]
header = ['OBSERVAÇÃO','TIPO']
siecc = pd.DataFrame(columns=header)
un = df_Model['Unit(Product)']
LMA_Construction = pd.concat([lm, siecc, un], axis=1)
LMA_Construction['TIPO'] = 'I'
LMA_Construction['OBSERVAÇÃO'] = '-'

def submarino(sbr):
  if sbr == '11':
    return '53A'
  elif sbr == '12':
    return '53B'
  elif sbr == '13':
    return '53C'
  elif sbr == '14':
    return '53D'
  else:
    return 'Erro na estrutura do CC'

sub = submarino(SBR) + '-'

conta = 0

for local in LMA_Construction['Number(Related product lot(s))']:
  LMA_Construction['Number(Related product lot(s))'].iloc[conta] = sub + local[4::]
  conta = conta + 1

conta = 0

for local in LMA_Construction['Industrial marker(Mounted Product)']:
  LMA_Construction['Industrial marker(Mounted Product)'].iloc[conta] = sub + local
  conta = conta + 1

conta = 0

for local in LMA_Construction['Number(Mounted Product)']:
  LMA_Construction['Number(Mounted Product)'].iloc[conta] = sub + local[4:12:]
  conta = conta + 1

LMA_Construction['Quantity provided(Product)'].fillna('1', inplace=True)

LMA_Construction.fillna('-', inplace=True)

LMA_Construction

df = LMA_Construction.head(1)

for a in df.index:
  df.rename(index={a:0}, inplace=True)
  
#Exluindo Linha Por Index
df.drop([0, 0]) 

df.drop([0, 0], inplace=True)

for i in Teste_EQ['Industrial Mark']:
  new_df = LMA_Construction[LMA_Construction['Number(Related product lot(s))'] == '53A' + i]
  #print(new_df)
  df = df.append(pd.concat([new_df]))

df


LMA_Construction

def ajustes1(teste, cont):
  conta = 0
  if teste != '-':
    return '-'
  else:
    return LMA_Construction['Number(Related product lot(s))'].iloc[cont]
  
  conta = conta + 1

    
ajustes1('sddsd', 1)
  


def ajustes2(teste, cont):
  conta = 0 
  
  if teste != '-':
    return '-'
  else:
    return LMA_Construction['Designation(Item).1'].iloc[cont]
 
  conta = conta + 1
    
ajustes2('sddsd', 1)

#xxx

conta = 0

for a in LMA_Construction['Number(Item).1']:
    LMA_Construction['Number(Related product lot(s))'].iloc[conta] = ajustes1(a, conta)
    print(a , '= Posição ', conta)
    conta = conta + 1
  

conta = 0

for a in LMA_Construction['Number(Item).1']:
    LMA_Construction['Designation(Mounted Product)'].iloc[conta] = ajustes2(a, conta)
    print(a , '= Posição ', conta)
    conta = conta + 1

LMA_Construction
