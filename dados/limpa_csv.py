#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir, makedirs
from os.path import isfile, join
import sys, os


mypath = './'

newdir = './arquivos_modificados/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

if not os.path.exists(newdir):
    os.makedirs(newdir)

for file in onlyfiles:
    nome_raw = file[:-4]
    novo_nome = nome_raw +'_limpo.csv'    
    novo_arquivo = open(newdir+novo_nome, "a")
    with open(file) as arquivo:
        content = arquivo.readlines()
        try:
            palavra = ''.join(content).replace(';', ',')
        except Exception as e:
            print(e)
            print('Nao foi possivel trocar ; por , .')
            
        try:            
            palavra2 = ''.join(palavra).replace('-', ';')
        except Exception as e:
            print(e)
            print('Nao foi possivel trocar - por ; .')
        
        
        novo_arquivo.write(palavra2)
        
        novo_arquivo.close()
        #print(novo_nome)
        #print(palavra)
        arquivo.close()
    