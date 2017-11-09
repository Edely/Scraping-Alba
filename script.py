#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys, argparse, logging, os, random, urllib, urllib2, common
import mechanize, urlparse, json, cookielib, re
from lista_deputados import deputados
#CONSTANTS
url_inicial = 'http://www.al.ba.gov.br/transparencia/prestacao-de-contas'


'''
> escolher deputado ou raspar todo o conteudo

> abrir pagina
    http://www.al.ba.gov.br/transparencia/prestacao-de-contasscip

> selecionar deputado ( Itera todas as 60 opçoes )
    > selecionar ano
        >selecionar mes
        
> raspar categoria e valor

> salvar em arquivo csv/sql
'''

br = mechanize.Browser()
pagina = br.open(url_inicial).read()

for form in br.forms():
    if form.attrs.get('action') == 'prestacao-de-contas':
        br.form = form
        
def menu_deputados():
    for k,v in deputados:
        print k + ' - ' + v

def abre_pagina(args):
    br = mechanize.Browser()
    pagina = br.open(url_inicial).read()
    
    for form in br.forms():
        if form.attrs.get('action') == 'prestacao-de-contas':
            br.form = form
            
    #prestacao-de-contas
    
    #caminho para deputado
    
    #caminho para mes
    
    #caminho para ano
    
    '''
    pegar o deputado, ano e mes
    se uma dessas opçoes nao for definida, entao cai no default
    sendo :
        deputado == todos
        ano == todos
        mes == todos
    '''
    
    
    if args.deputado == 'todos':
        #pesquisa todos:
        print 'legal'
    else:
        #pesquisa so o deputado
        print 'legal'
    

def main(args):
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
    parser.add_argument('--lista', help="A lista de deputados e seus respectivos codigos", action="menu_deputados")
    args = parser.parse_args()
    
print(args)
















