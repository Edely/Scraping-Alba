#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys, argparse, logging, os, random, urllib, urllib2, common
import mechanize, urlparse, json, cookielib, re
from lista_deputados import deputados



             
def acessa_form(deputy, year, month, form, br, k=0):
    form['deputado'] = [str(deputy)]
    form['mes'] = [str(month)]
    form['ano'] = [str(year)]

    br.submit()
    resposta = br.response().read()
    print(resposta)
    soup_dados = BeautifulSoup(resposta, "lxml") 
    
    [strong.extract() for strong in soup_dados('strong')]
    
    [clearFloat.decompose() for clearFloat in soup_dados.find_all("div", {'class': 'clearFloat'})]
         
    
    dados = soup_dados.find_all('div', 'linha-prop')
    if len(dados) != 0:
        nome_arquivo = "dados_alba_"+str(k)+".csv"
        arquivo = open(nome_arquivo, "a+")
            
    i = 0
    for item in dados:
        if i != 0:
            arquivo.write(str(k)+'-'+deputados[str(deputy)] +'-')
            infos_item = item.find_all('div')
            j = 1
            for infos in infos_item:
                a = infos.text.lstrip()
                palavras = a.split()                
                if j == 1:
                    arquivo.write(palavras[0]+'- ')
                    arquivo.write(palavras[2]+'- ')
                elif j == 2:
                    arquivo.write(a.strip().encode("utf-8") +'- ')
                elif j == 3:
                    a = a[3:]
                    arquivo.write(a.strip().encode("utf-8"))
                j = j + 1
        i+=1
        arquivo.write('\n')
              
    arquivo.close()
        
def abre_pagina(args):
    url_inicial = 'http://www.al.ba.gov.br/transparencia/prestacao-de-contas'
    br = mechanize.Browser()
    try:
        pagina = br.open(url_inicial, timeout=60).read()
        br.set_handle_robots(False)
    except(urllib2.URLError) as e:
        print('erro de conexao 2')
        print(e)
        sys.exit(0)
    
    for form in br.forms():
        if form.attrs.get('action') == 'prestacao-de-contas':
            br.form = form
    
    if args.deputado != 'todos':
        deputy = str(args.deputado)
    else:
        for k,v in deputados.items():
            try:
                print(deputados[k])
            
                for form in br.forms():
                    if form.attrs.get('action') == 'prestacao-de-contas':
                        br.form = form
                        
                deputy = str(k)
                year = str(0)
                month = str(0)
                acessa_form(deputy, year, month, form, br, k)
            except Exception as e:
                print(e)
        
    if args.ano != 'todos':
        year = str(args.ano)
    else:
        year = str(0)
    
    if args.mes != 'todos':
        month = str(args.mes)
    else:
        month = str(0)
    k=0
    return {"deputy": deputy, "year": year, "month": month, "form": form, "br": br, "deputado": args.deputado}
    
def main(args):
    print('===========')
    print(args)
    
    br, cj = common.initialize_browser()
    try:
        abre_pagina(deputado)
    except urllib2.URLError:
        logging.critical("Erro na conexão com a internet, tente novamente mais tarde")
        sys.exit(1)
    except KeyboardInterrupt:
        logging.critical("Fechando o programa.")
        sys.exit(0)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parametros da raspagem da prestacao de contas do site da ALBA')   
    parser.add_argument('--deputado', help="O codigo do deputado a ser pesquisado.", default='todos')
    parser.add_argument('--ano', help="O mes a ser pesquisado.", default='todos')
    parser.add_argument('--mes', help="O ano a ser pesquisado.", default='todos')
    parser.add_argument('--lista', help="A lista de deputados e seus respectivos codigos", default='esconder')
    args = parser.parse_args()
    
    if args.lista == 'mostrar':
        for k,v in deputados.items():
            print( k + ' - ' + v)
    print('++++++++++++')
    print(args)
    resultado = abre_pagina(args)
    
    print(resultado['deputy'], resultado['year'], resultado['month'], resultado['form'], resultado['br'], resultado['deputado'])
    acessa_form(resultado['deputy'], resultado['year'], resultado['month'], resultado['form'], resultado['br'], resultado['deputado'])
                        
   