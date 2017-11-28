#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys, argparse, logging, os, random, urllib, urllib2, common
import mechanize, urlparse, json, cookielib, re
from lista_deputados import deputados
#CONSTANTS
url_inicial = 'http://www.al.ba.gov.br/transparencia/prestacao-de-contas'

print('a')

br = mechanize.Browser()
try:
    pagina = br.open(url_inicial, timeout=60).read()
except(urllib2.URLError) as e:
    print('erro de conexao 1')
    print(e)
    sys.exit(0)
    

for form in br.forms():
    if form.attrs.get('action') == 'prestacao-de-contas':
        br.form = form
        
    #print(form)
        
def abre_pagina(args):
    print('b')
    #print(args)
    
    br = mechanize.Browser()
    try:
        print('c')
        pagina = br.open(url_inicial, timeout=60).read()
    except(urllib2.URLError) as e:
        print('erro de conexao 2')
        print(e)
        sys.exit(0)
    
    for form in br.forms():
        if form.attrs.get('action') == 'prestacao-de-contas':
            br.form = form
    
    print('e')
    
    #parametros_pesquisa = {'deputado': 'todos', 'ano': 'todos', 'mes': 'todos'}
    
    if args.deputado != 'todos':
        deputy = str(args.deputado)
    else:
        deputy = str(0)
        
    if args.ano != 'todos':
        year = str(args.ano)
    else:
        year = str(0)
    
    if args.mes != 'todos':
        month = str(args.mes)
    else:
        month = str(0)
        
    #enviar = br.submit()
    print('f')
    
    #aqui entrar o loop para acessar os dados especificamente
    
    #deputado        
#    def itera_forms():        
#        while(indice_deputados < len(deputados.items())):
#            print(indice_deputado)
        
    #ano
    #mes
    
    acessa_form(deputy, year, month, form, br)
        
    print('g')
    
    pagina_resposta = br.response().read()
    print('h')
    
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
    parser.add_argument('--lista', help="A lista de deputados e seus respectivos codigos", default='esconder')
    args = parser.parse_args()
    
    if args.lista == 'mostrar':
        for k,v in deputados.items():
            print( k + ' - ' + v)
                        
                
def acessa_form(deputy, year, month, form, br):
    form['deputado'] = [str(deputy)]
    form['mes'] = [str(month)]
    form['ano'] = [str(year)]

    enviar = br.submit()
    print('legal')
    soup_dados = BeautifulSoup(br.response().read(), "html5lib")       
    dados = soup_dados.find_all('div', 'linha-prop')
    if len(dados) != 0:
        arquivo = open("dados_alba.csv", "a+")
            
    i = 0
    for item in dados:
        if i != 0:
            infos_item = item.find_all('div')
            for infos in infos_item:
                print infos.text
                
            print("""======""")
            #print(item)
            
            #   print("item")
        i+=1
              
    
abre_pagina(args)


#
#
#<div class="linha-prop">
#  <div class="col-prop1">
#      <strong>Mês / Ano</strong>
#       01 / 2015
#  </div>
#  <div class="col-prop2">
#      <strong>Categoria</strong>
#      Aquisição ou locação de software; serviços postais  e de segurança; assinaturas de publicações; TV a cabo ou similar; acesso à Internet; e locação de móveis e equipamentos. Telefones.
#  </div>
#  <div class="col-prop3">
#     <strong>Valor (R$)</strong>
#     R$ 486.08
#  </div>
#  <div class="clearFloat"></div>
#</div>
#<div class="linha-prop">
#  <div class="col-prop1">
#      <strong>Mês / Ano</strong>
#       01 / 2015
#  </div>
#  <div class="col-prop2">
#      <strong>Categoria</strong>
#      Consultorias, assessorias, pesquisas  e trabalhos técnicos
#  </div>
#  <div class="col-prop3">
#     <strong>Valor (R$)</strong>
#     R$ 32500
#  </div>
#  <div class="clearFloat"></div>
#</div>
