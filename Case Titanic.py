#%%

# Importa as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#%% 
# Importa o arquivo .csv em forma DataFrame
df1 = pd.read_csv('test.csv')
df2 = pd.read_csv('train.csv')


#%% 
# Visualiza df1 (test)
df1


#%% 
# Visualiza df2 (train)
df2


#%% 
df1.describe()


#%% 
# Descreve as colunas de dados brevemente para breve análise
df2.describe()


#%%
# Visualiza todos os registros com valores menores que 1 na coluna idade no df1 (test)
df1.loc[df1['Age'] < 1]


#%%
# Visualiza todos os registros com valores menores que 1 na coluna idade no df2 (train)
df2.loc[df2['Age'] < 1]


#%%
# Visualiza todos os registros com que possuam terminação .5 na coluna idade no df1 (test)
df1[df1['Age'] % 1 == 0.5]


#%%
# Visualiza todos os registros com que possuam terminação .5 na coluna idade no df2 (train)
df2[df2['Age'] % 1 == 0.5]


#%%
# Tira o valor .5 de algumas idades
def remove_half(num):
    if num % 1 == 0.5:
        return int(num)
    else:
        return num

df1['Age'] = df1['Age'].apply(remove_half)
df2['Age'] = df2['Age'].apply(remove_half)

# Confirma se a mudança ocorreu no df1 (test)
df1[df1.index == 0]


#%%
# Confirma se a mudança ocorreu no df2 (train)
df2[df2.index == 57]


#%%
# Visualiza todos os registros com valores faltantes na coluna idade no df1 (test)
df1[df1['Age'].isnull()]


#%%
# Visualiza todos os registros com valores faltantes na coluna idade no df2 (train)
df2[df2['Age'].isnull()]


# %%
# Calcula a media de idade de cada genero do df1 (test)
med_idade_homem = df1.loc[df1["Sex"] == "male", "Age"].mean()
media_idade_mulher = df1.loc[df1["Sex"] == "female", "Age"].mean()
med_idade_homem = int(med_idade_homem)
media_idade_mulher = int(media_idade_mulher)
print (" média de idade dos homens no test: ",med_idade_homem)
print (" média de idade das mulheres test: ",media_idade_mulher)


#%%
# Substitui os valores faltantes pela média de cada gênero no df1 (test)
df1.loc[(df1["Sex"] == "male") & (df1["Age"].isnull()), "Age"] = med_idade_homem
df1.loc[(df1["Sex"] == "female") & (df1["Age"].isnull()), "Age"] = media_idade_mulher

# Confirma se a mudança ocorreu 
df1.loc[(df1["Sex"] == "male") & (df1["Age"] == med_idade_homem)]


# %%
# Calcula a media de idade de cada genero no df2 (dataframe train)
med_idade_homem = df2.loc[df2["Sex"] == "male", "Age"].mean()
media_idade_mulher = df2.loc[df2["Sex"] == "female", "Age"].mean()
med_idade_homem = int(med_idade_homem)
media_idade_mulher = int(media_idade_mulher)
print (" média de idade dos homens no train: ",med_idade_homem)
print (" média de idade das mulheres train: ",media_idade_mulher)


#%%
# Substitui os valores faltantes pela média de cada gênero no df2 (dataframe train)
df2.loc[(df2["Sex"] == "male") & (df2["Age"].isnull()), "Age"] = med_idade_homem
df2.loc[(df2["Sex"] == "female") & (df2["Age"].isnull()), "Age"] = media_idade_mulher

# Confirma se a mudança ocorreu 
df2.loc[(df2["Sex"] == "male") & (df2["Age"] == med_idade_homem)]


#%%
# Cria uma nova coluna indicando se a pessoa é mulher(1) ou não (0) no df1 (test)
df1['IsFemale'] = df1['Sex'].apply((lambda x: 1 if x == 'female' else 0)) 
df2['IsFemale'] = df2['Sex'].apply((lambda x: 1 if x == 'female' else 0)) 
df1


#%%
# Cria uma nova coluna indicando se a pessoa estava na primeira classe(1) ou não(0) no df1 (test)
df1['IsPclass1'] = df1['Pclass'].apply(lambda x: 1 if x == 1 else 0)
df2['IsPclass1'] = df2['Pclass'].apply(lambda x: 1 if x == 1 else 0)
df1


#%%
# Cria uma nova coluna indicando se a pessoa estava na segunda classe(1) ou não(0) no df1 (test)
df1['IsPclass2'] = df1['Pclass'].apply(lambda x: 1 if x == 2 else 0)
df2['IsPclass2'] = df2['Pclass'].apply(lambda x: 1 if x == 2 else 0)
df1


#%%
# Função que calcula g(x)
def g(row):
    isFemale = row['IsFemale']
    isPclass1 = row['IsPclass1']
    isPclass2 = row['IsPclass2']
    Age = row['Age']
    return -1.33 + 2.55*isFemale + 1.27*isPclass2 + 2.58*isPclass1 - 0.04*Age

# Insere o valor g(x) em uma nova coluna no df1 (test)
df1['g(x)'] = df1.apply(lambda row: g(row), axis=1)
df1


#%%

# Adapta os valores da regressão para responder a pergunta
def adapt(g):
    if g >= 1:
        g = 3
    else:
        g = 2
    return g

# Cria uma nova coluna e preenche como possivel sobrevivente (3) ou não(2) no df1 (test)
df1['SurvivedPredicted'] = df1['g(x)'].apply(adapt)
df1


#%%
# Visualiza todos os possiveis sobreviventes do df1 (test)
df1[df1['SurvivedPredicted'] == 3]


#%%
# Visualiza o registro do unico homem que sobreviveria do df 1(test)
df1.loc[(df1['SurvivedPredicted'] == 3) & (df1['Sex'] == 'male')]


#%%
# Fundindo os 2 dataframes (train e test) e visualizando o dataframe resultante

df = pd.concat([df2, df1], axis=0,ignore_index=True)
df




# GRÁFICOS





#%%
# ----------------- PRIMEIRO GRÁFICO ----------------- 
# Plotagem do df 1(test)

percentual_embarked = df1['Embarked'].value_counts(normalize=True) * 100
label = ['Southampton', 'Cherbourg', 'Queenstown']

# Cria o gráfico 
plt.pie(percentual_embarked, labels = label, autopct='%1.2f%%',startangle=90)

# Adiciona título
plt.title('Percentual de pessoas embarcadas em cada local')
plt.show()


#%% 
# Plotagem do df 2(train)  

percentual_embarked = df2['Embarked'].value_counts(normalize=True) * 100
label = ['Southampton', 'Cherbourg', 'Queenstown']

# Cria o gráfico 
plt.pie(percentual_embarked, labels = label, autopct='%1.2f%%',startangle=90)

# Adiciona título
plt.title('Percentual de pessoas embarcadas em cada local')
plt.show()


#%%
# ----------------- SEGUNDO GRÁFICO ----------------- 
# Plotagem do df 1(test)

pessoas_por_classe = df1['Pclass'].value_counts()
label = ['3rdClass','1stClass','2ndClass']

# Cria o gráfico 
plt.pie(pessoas_por_classe, labels=label, autopct='%1.2f%%',startangle=90)

# Adiciona título
plt.title('Número de pessoas a bordo por classe')
plt.show()


#%%
# Plotagem do df 2(train)  

pessoas_por_classe = df2['Pclass'].value_counts()
label = ['3rdClass','1stClass','2ndClass']

# Cria o gráfico 
plt.pie(pessoas_por_classe, labels=label, autopct='%1.2f%%',startangle=90)

# Adiciona título
plt.title('Número de pessoas a bordo por classe')
plt.show()





#%%
# ----------------- TERCEIRO GRÁFICO ----------------- 
# Plotagem do df 1(test)


SibSp_count = df1['SibSp'].value_counts()

# Calcula o total de frequências
totalSibSp_count = SibSp_count.sum()

# Cria o gráfico de barras verticais
plt.bar(SibSp_count.index, SibSp_count.values)

# Adiciona a porcentagem de cada barra em relação ao total
for i, freq in enumerate(SibSp_count.values):
    porcentagem = 100 * freq / totalSibSp_count
    plt.text(SibSp_count.index[i], freq + 1, f'{porcentagem:.1f}%', ha='center')


# adiciona título e rótulos dos eixos
plt.title(' Contagem do número de pessoas com irmãos/cônjuges a bordo do návio')
plt.xlabel('Número de irmãos/conjuges abordo')
plt.ylabel('Contagem de irmaõs/conjuges')
plt.show()

#%%
# Plotagem do df 2(train)


SibSp_count = df2['SibSp'].value_counts()

# Calcula o total de frequências
totalSibSp_count = SibSp_count.sum()

# Cria o gráfico de barras verticais
plt.bar(SibSp_count.index, SibSp_count.values)

# adiciona a porcentagem de cada barra em relação ao total
for i, freq in enumerate(SibSp_count.values):
    porcentagem = 100 * freq / totalSibSp_count
    plt.text(SibSp_count.index[i], freq + 1, f'{porcentagem:.1f}%', ha='center')


# Adiciona título e rótulos dos eixos
plt.title(' Contagem do número de pessoas com irmãos/cônjuges a bordo do návio')
plt.xlabel('Número de irmãos/conjuges abordo')
plt.ylabel('Contagem de irmaõs/conjuges')
plt.show()





#%%
#  ----------------- QUARTO GRÁFICO -----------------
# Plotagem do df 1(test)

parch_count = df1['Parch'].value_counts()

# Calcula o total de frequências
totalParch_count = parch_count.sum()

# Cria o gráfico de barras verticais
plt.bar(parch_count.index, parch_count.values)

# Adiciona a porcentagem de cada barra em relação ao total
for i, freq in enumerate(parch_count.values):
    porcentagem = 100 * freq / totalParch_count
    plt.text(parch_count.index[i], freq + 1, f'{porcentagem:.1f}%', ha='center')

# adiciona título e rótulos dos eixos
plt.title('Contagem do número de pessoas com pais/filhos a bordo do návio')
plt.xlabel('Número de pais/filhos a bordo')
plt.ylabel('Contagem pais/filhos')
plt.show()



#%%
# Plotagem do df 2(train)

parch_count = df2['Parch'].value_counts()

# Calcula o total de frequências
totalParch_count = parch_count.sum()

# Cria o gráfico de barras verticais
plt.bar(parch_count.index, parch_count.values)

# Adiciona a porcentagem de cada barra em relação ao total
for i, freq in enumerate(parch_count.values):
    porcentagem = 100 * freq / totalParch_count
    plt.text(parch_count.index[i], freq + 1, f'{porcentagem:.1f}%', ha='center')

# adiciona título e rótulos dos eixos
plt.title('Contagem do número de pessoas com pais/filhos a bordo do návio')
plt.xlabel('Número de pais/filhos a bordo')
plt.ylabel('Contagem pais/filhos')
plt.show()



#%%
# ----------------- QUINTO GRÁFICO -----------------   
# Plotagem do df 1(test)

media_idade = df1['Age'].mean()

# Configurando o histograma
sns.set_style('whitegrid')
pessoas_count = df1['PassengerId'].value_counts()
sns.histplot(data=pessoas_count, x=df1['Age'], bins=range(0, 90, 10), kde=True)

# Configurando o título e legendas dos eixos
plt.title('Número de Passageiros por Idade')
plt.xlabel('Idade (anos)')
plt.ylabel('Número de Passageiros')
plt.show()



#%%
# Plotagem do df 2(train)

media_idade = df2['Age'].mean()

# Configurando o histograma
sns.set_style('whitegrid')
pessoas_count = df2['PassengerId'].value_counts()
sns.histplot(data=pessoas_count, x=df2['Age'], bins=range(0, 90, 10), kde=True)

# Configurando o título e legendas dos eixos
plt.title('Número de Passageiros por Idade')
plt.xlabel('Idade (anos)')
plt.ylabel('Número de Passageiros')
plt.show()




#%%
# SEXTO GRÁFICO (6.1)

count = df.groupby('Survived')['PassengerId'].count()

# Calculando a porcentagem de cada categoria em relação ao total
total_count = count.sum()
porcentagens1 = [f'{100*freq/total_count:.1f}%' for freq in count.values]

# Configurando o gráfico
plt.bar(count.index, count.values, color=['red','blue'])
for i, freq in enumerate(count.values):
    plt.text(count.index[i], freq + 1, porcentagens1[i], ha='center')

plt.xticks([0, 1], ['Morreram', 'Sobreviveram'])
plt.ylabel('Contagem de Passageiros')
plt.title('Número de Passageiros que morreram e que sobreviveram')
plt.show()



#%%
# SEXTO GRÁFICO (6.2)

count = df.groupby('SurvivedPredicted')['PassengerId'].count()
total_count = count.sum()
porcentagens2 = [f'{100*freq/total_count:.1f}%' for freq in count.values]

# Configurando o gráfico
plt.bar(count.index, count.values, color=['red','blue'])
plt.bar(count.index, count.values, color=['red','blue'])
for i, freq in enumerate(count.values):
    plt.text(count.index[i], freq + 1, porcentagens2[i], ha='center')

plt.xticks([2, 3], ['Morreriam', 'Sobreviveriam'])
plt.ylabel('Contagem de Passageiros')
plt.title('Número de Passageiros que morreriam e que sobreviveriam')
plt.show()



#%%
# SEXTO GRÁFICO (6.3)

countSurvived = df.groupby(['Survived'])['PassengerId'].count()
countSurvivedPredicted = df.groupby('SurvivedPredicted')['PassengerId'].count()
totalCountSurvived = countSurvived.sum()
totalCountSurvivedPredicted = countSurvivedPredicted.sum()
porcentagens1 = [f'{100*freq/totalCountSurvived:.1f}%' for freq in countSurvived.values]
porcentagens2 = [f'{100*freq/totalCountSurvivedPredicted:.1f}%' for freq in countSurvivedPredicted.values]

# Configurando o gráfico
plt.bar(countSurvived.index, countSurvived.values, color=['red', 'blue'])
for i, freq in enumerate(countSurvived.values):
    plt.text(countSurvived.index[i], freq + 1, porcentagens1[i], ha='center')

plt.bar(countSurvivedPredicted.index, countSurvivedPredicted.values, color=['red', 'blue',])
for i, freq in enumerate(countSurvivedPredicted.values):
    plt.text(countSurvivedPredicted.index[i], freq + 1, porcentagens2[i], ha='center')


plt.xticks([0, 1, 2, 3], ['Morreram', 'Sobreviveram', 'Morreriam', 'Sobreviveriam'])
plt.ylabel('Contagem de Passageiros')
plt.title('Número de passageiros por sobrevivência real e prevista')
plt.show()




#%%
# SÉTIMO GRÁFICO (7.1)

sobreviveram = df.groupby('Pclass')['Survived'].sum()
morreram = df.groupby('Pclass')['Survived'].count() - sobreviveram

# Configuração do gráfico
plt.bar([0, 1, 2], morreram, color='red', label='Morreram')
plt.bar([0, 1, 2], sobreviveram, color='green', bottom=morreram, label='Sobreviveram')
plt.xticks([0, 1, 2], ['1stClass', '2ndClass', '3rdClass'])
plt.ylabel('Número de Pessoas')
plt.legend()
plt.show()



#%%
# SÉTIMO GRÁFICO (7.2)

sobreviveriam = df.groupby('Pclass')['SurvivedPredicted'].apply(lambda x: (x == 3).sum())
morreriam = df.groupby('Pclass')['SurvivedPredicted'].count() - sobreviveriam


# Configuração do gráfico
plt.bar([0, 1, 2], morreriam, color='red', label='Morreriam')
plt.bar([0, 1, 2], sobreviveriam, color='green', bottom=morreriam, label='Sobreviveriam')
plt.xticks([0, 1, 2], ['1stClass', '2ndClass', '3rdClass'])
plt.ylabel('Número de Pessoas')
plt.legend()
plt.show()



#%%
# SÉTIMO GRÁFICO (7.3)

sobreviveram = df.groupby('Pclass')['Survived'].sum()
morreram = df.groupby('Pclass')['Survived'].count() - sobreviveram
sobreviveriam = df.groupby('Pclass')['SurvivedPredicted'].apply(lambda x: (x == 3).sum())
morreriam = df.groupby('Pclass')['SurvivedPredicted'].count() - sobreviveriam

# Configuração do gráfico
plt.bar([0, 1, 2], morreram, color='red', label='Morreram')
plt.bar([0, 1, 2], sobreviveram, color='green', bottom=morreram, label='Sobreviveram')
plt.bar([4, 5, 6], morreriam, color='purple', label='Morreriam')
plt.bar([4, 5, 6], sobreviveriam, color='blue', bottom=morreriam, label='Sobreviveriam')
plt.xticks([0, 1, 2, 4, 5, 6], ['1stClass', '2ndClass', '3rdClass','1stClass','2ndClass','3rdClass'])
plt.ylabel('Número de Pessoas')
plt.legend()
plt.show()




#%%
# OITAVO GRÁFICO (8.1)


sobreviveram = df.groupby('Sex')['Survived'].sum()
morreram = df.groupby('Sex')['Survived'].count() - sobreviveram

# Configuração do gráfico
plt.bar([0, 1], morreram, color='green', label='Morreram')
plt.bar([0, 1], sobreviveram, color='blue', bottom=morreram, label='Sobreviveram')
plt.xticks([0, 1], ['female','male'])
plt.ylabel('Número de Pessoas')
plt.legend()
plt.show()

#%%
# OITAVO GRÁFICO (8.2)

sobreviveriam = df.groupby('Sex')['SurvivedPredicted'].apply(lambda x: (x == 3).sum())
morreriam = df.groupby('Sex')['SurvivedPredicted'].count() - sobreviveriam

# Configuração do gráfico
plt.bar([0, 1], morreriam, color='green', label='Morreriam')
plt.bar([0, 1], sobreviveriam, color='blue', bottom=morreriam, label='Sobreviveriam')
plt.xticks([0, 1], ['female','male'])
plt.ylabel('Número de Pessoas')
plt.legend()
plt.show()

#%%
# OITAVO GRÁFICO (8.3)

sobreviveram = df.groupby('Sex')['Survived'].sum()
morreram = df.groupby('Sex')['Survived'].count() - sobreviveram
sobreviveriam = df.groupby('Sex')['SurvivedPredicted'].apply(lambda x: (x == 3).sum())
morreriam = df.groupby('Sex')['SurvivedPredicted'].count() - sobreviveriam

# Configuração do gráfico
plt.bar([0, 1], morreram, color='green', label='Morreram')
plt.bar([0, 1], sobreviveram, color='blue', bottom=morreram, label='Sobreviveram')
plt.bar([3, 4], morreriam, color='red', label='Morreriam')
plt.bar([3, 4], sobreviveriam, color='purple', bottom=morreriam, label='Sobreviveriam')
plt.xticks([0, 1, 3, 4], ['female','male','female','male'])
plt.ylabel('Número de Pessoas')
plt.legend()
plt.show()

#%%
df[(df['Sex'] == 'male') & (df['SurvivedPredicted'] == 3) ]

#%%