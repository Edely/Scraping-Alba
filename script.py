#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys, argparse, logging, os, random, urllib, urllib2, common
import mechanize, urlparse, json, cookielib, re

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



def abre_pagina(deputado):
    br = mechanize.Browser()
    pagina = br.open(url_inicial).read()
    
    if deputado == 'todos':
        #pesquisa todos:
    else:
        #pesquisa so o deputado
    

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
    pass     