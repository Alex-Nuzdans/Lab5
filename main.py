import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
matplotlib.use('Agg')
from matplotlib.colors import ListedColormap
import seaborn as sns
import math

def load_data(name,collons):
    return pd.read_csv(name,sep=';',usecols=collons,encoding='utf-8')

def diogramm_T_U(df):
    colors=["red","blue"]
    cond=df['N']=="100%."
    cmap_binary = ListedColormap(colors)
    plt.scatter(df['T'],df['U'],c=cond, cmap=cmap_binary, alpha=0.5)
    plt.xlabel("Температура")
    plt.ylabel("Влажность воздуха")
    plt.title("Диаграмма рассеяния")
    plt.savefig('T_U_Diogramm.png')
    plt.clf()

def diogramm_T_U_1(df):
    plt.scatter(df['T'],df['U'],color="red", alpha=0.5)
    plt.xlabel("Температура")
    plt.ylabel("Влажность воздуха")
    plt.title("Диаграмма рассеяния")
    plt.savefig('T_U_Diogramm_1.png')
    plt.clf()

def diogramm_Time_T(df):

    sns.set_style("whitegrid")
    sns.lineplot(data=df, x="T", y="Местное время в Перми", marker='o', linewidth=2.5)
    plt.xlabel("Температура")
    plt.ylabel("Местное время в Перми")
    plt.title("Обычный граф")
    plt.savefig('Time_T_Diogramm.png')
    plt.clf()

def diogramm_meanT_month(df):
    result=df.groupby('Месяц')['T'].mean().reset_index(name='Tm')
    sns.barplot(data=result, x='Месяц', y='Tm', hue='Месяц', palette='viridis', legend=False)
    plt.xlabel("Месяц")
    plt.ylabel("Средняя Температура")
    plt.title("Столбчатая диограмма")
    plt.savefig('mT_M_Diogramm.png')
    plt.clf()

def diogramm_countN_N(df):
    plt.figure(figsize=(50, 6))
    result=df.groupby('N')['N'].count().reset_index(name='count')
    sns.barplot(data=result, x='count', y='N', hue='N', palette='viridis', legend=False)
    plt.xlabel("Количество")
    plt.ylabel("Варианты облочности")
    plt.title("Ленточная диограмма")
    plt.savefig('сN_N_Diogramm.png')
    plt.clf()

def get_month(df):
    result=[]
    for i in df['Местное время в Перми']:
        result.append(i.split('.')[1])
    return result

def diogramm_interval_T(df):
    plt.figure(figsize=(12, 6))
    plt.hist(df['T'],10)
    plt.xlabel("Температура")
    plt.ylabel("Количество")
    plt.title("Гистограмма")
    plt.savefig('In_T_Diogramm.png')
    plt.clf()

def diogramm_boxplot(df):
    bins = [0, 5, 15, df['VV'].max()]
    labels = ['< 5', '5-15', '≥ 15']
    df['VV_Range'] = pd.cut(df['VV'], bins=bins, labels=labels, include_lowest=True)
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='VV_Range', y='P')
    plt.ylabel("Атмосферное давление")
    plt.xlabel("Диапазоны дальности видимости")
    plt.title("Диограмма с усами")
    plt.savefig('boxplot_Diogramm.png')
    plt.clf()

def diogramm_pie(df):
    plt.figure(figsize=(12, 10))
    result=df.groupby('H')['H'].count().reset_index(name='count')
    plt.pie(result['count'], labels=result['H'], autopct='%1.1f%%')
    plt.title("Круговая диограмма")
    plt.savefig('pie_Diogramm.png')
    plt.clf()

'''
def intervals(df):
    l=round((df['T'].max()-df['T'].min())/10)
    one=df['T'].min()+l
    temp=[str(df['T'].min())+" — "+str(one)]
    for i in range(9):
        two=one+l
        temp.append(str(round(one,2))+" — "+str(round(two,2)))
        one=two
    return temp
'''

if __name__ == '__main__':
    df= load_data('weather1.csv',
                    ["Местное время в Перми",'T','P','U',
                    'Ff','N','H','VV'])

    print(df['Местное время в Перми'][0].split('.')[1])
    df["Месяц"]=get_month(df)
    print(df.head(10))
    diogramm_T_U_1(df)
    diogramm_T_U(df)
    diogramm_Time_T(df)
    diogramm_meanT_month(df)
    diogramm_countN_N(df)
    diogramm_interval_T(df)
    diogramm_boxplot(df)
    diogramm_pie(df)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
