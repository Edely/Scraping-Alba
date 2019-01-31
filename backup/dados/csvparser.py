#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import listdir, makedirs
from os.path import isfile, join
import sys, os, csv

meses = [[],[],[],[],[],[],[],[],[],[],[],[]]

caminho_arquivo = './arquivos_modificados/merged.csv'

arquivo = open(caminho_arquivo, encoding='utf-8')
arquivo_csv = csv.reader(arquivo, delimiter=';')
for row in arquivo_csv:
    if row != []:
        mes = row[2]
        meses[int(mes)-1].append(row)

for mes in meses:
    tamanho = len(mes)
    #print(tamanho)
    for linha in mes:
        print(linha[0])
        print('================')
        
    # for counter in range(0, tamanho):
    #     #print(mes[counter])
    #     #sys.exit(0)
    #     #print(mes[counter][0])
    #     if counter != tamanho - 1:
    #         if((mes[counter][4] == ' Assessorias') or (mes[counter][4] == ' Consultorias') or (mes[counter][4] == ' Pesquisas') or (mes[counter][4] == ' Trabalhos Técnicos')):
    #             if(mes[counter][0] == mes[counter+1][0]) and (mes[counter][3] == mes[counter+1][3]):
    #                 novo_valor =  float(mes[counter+1][5]) + float(mes[counter][5])
    #                 mes[counter][5] = novo_valor
                    # print(mes[counter])
                    # print(mes[counter][5])
                    # print(mes[counter+1])
                    # print(mes[counter+1][5])
                    # print(novo_valor)
                    # print(mes[counter][5])

#['923801', 'Dep. Samuel Júnior', '12', ' 2017', ' Assessorias', ' 9750']
#['923801', 'Dep. Samuel Júnior', '12', ' 2017', ' Consultorias', ' 9750']
