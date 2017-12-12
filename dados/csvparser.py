#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import listdir, makedirs
from os.path import isfile, join
import sys, os, csv 

meses = [[],[],[],[],[],[],[],[],[],[],[],[]]

caminho_arquivo = './arquivos_modificados/dados_alba_901255_limpo.csv'

arquivo = open(caminho_arquivo, encoding='utf-8')
arquivo_csv = csv.reader(arquivo, delimiter=';')
for row in arquivo_csv:
    if row != []:
        mes = row[2]
        meses[int(mes)-1].append(row)
        
for mes in meses:
    