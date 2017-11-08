#!/usr/bin/env python
# -*- coding: utf-8 -*-

import locale
from locale import setlocale, LC_ALL
import unicodedata
import codecs
import time
import sys
import io
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locale.setlocale(locale.LC_ALL, 'pt_BR')

indice_inicio = int(sys.argv[1])
tamanho = int(sys.argv[2])

def manipula_formulario(indice_deputado, indice_ano, indice_mes):
    global deputado
    global mes
    global ano

    #seleciona deputado
    revela_deputado = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/form/div[2]/div[1]/div/div')
    seleciona_deputado = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/form/div[2]/div[1]/div/ul/li['+ str(indice_deputado) +']/a')



    revela_deputado.click()
    seleciona_deputado.click()

    deputado = seleciona_deputado.get_attribute('textContent')

    #seleciona mes
    revela_mes = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/form/div[2]/div[2]/div/div')
    seleciona_mes = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/form/div[2]/div[2]/div/ul/li['+ str(indice_mes) +']/a')

    revela_mes.click()
    seleciona_mes.click()
    mes = seleciona_mes.get_attribute('textContent')

    #seleciona ano
    revela_ano = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/form/div[2]/div[3]/div/div')
    seleciona_ano = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/form/div[2]/div[3]/div/ul/li['+ str(indice_ano)+']/a')

    revela_ano.click()
    seleciona_ano.click()
    ano = seleciona_ano.get_attribute('textContent')

    #submit
    submit = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/form/div[3]/input[1]')
    submit.click()


#lembrar de rever a forma como os indices para loop dos deputados e colocado

def loop_deputados(indice_deputado, indice_ano, indice_mes):

    #percorre por todos os deputados, anos e meses
    while (indice_deputado < 66):

        indice_ano = 1
    
        while (indice_ano <10):

            indice_mes = 1

            while(indice_mes < 13):
                #seleciona as informações no formulário
                manipula_formulario(indice_deputado, indice_ano, indice_mes)
                #copia dados da tabela de classe tbContas
                copia_dados_da_tabela()
                #copia dados da div com os valores totais
                copia_dados_da_div()
                #junto os dados num mesmo dictionary
                junta_dois_dicts(dict_tabela, dict_div)
                #renomeia as chaves do dictionary
                renomeia_keys()
                #transforma os valores em float
                converte_e_escreve_valores()
                #reabre a página
                driver.get(endereco)

                indice_mes += 1

            indice_ano += 1

        indice_deputado += 1

def copia_dados_da_tabela():

    cat = []
    val = []
    categorias = driver.find_elements_by_class_name("tdCategoria")
    for categoria in categorias:
        cat.append(categoria.text)

    valores = driver.find_elements_by_class_name("tdValor")
    for valor in valores:
        val.append(valor.text)

    global dict_tabela
    dict_tabela = dict(zip(cat, val))

def copia_dados_da_div():
    calval = []
    calcvalores = driver.find_elements_by_css_selector(".calcValores > p")
    for item in calcvalores:
        calval.append(item.text)
    #a depender do resultado, div pode ter dois ou três tags <p>
    if (len(calval) == 2):
        apresentado = str(calval[0])
        indenizado = str(calval[1])
    elif(len(calval) == 3 ):
        apresentado = str(calval[0])
        excedente = str(calval[1])
        indenizado = str(calval[2])
    else:
        print "Houve uma inconsistência no HTML. Cheque o código."
        exit()

    if(len(calval) == 2):
        key_apresentado, value_apresentado = apresentado.split(':')
        key_indenizado, value_indenizado = indenizado.split(':')
    elif(len(calval) == 3):
        key_apresentado, value_apresentado = apresentado.split(':')
        key_indenizado, value_indenizado = indenizado.split(':')
        key_excedente, value_excedente = excedente.split(':')

    global dict_div

    if(len(calval) == 2):
        dict_div = {key_apresentado: value_apresentado, key_indenizado: value_indenizado}
    elif(len(calval) == 3):
        dict_div = {key_apresentado: value_apresentado, key_indenizado: value_indenizado, key_excedente: value_excedente}

def junta_dois_dicts(primeiro, segundo):
    global dict_parcial
    dict_parcial = segundo.copy()
    dict_parcial.update(primeiro)

def renomeia_keys():
    global dict_completo
    dict_completo = {'imo':0.0, 'con':0.0, 'div':0.0,'loc':0.0, 'sof':0.0, 'exp':0.0, 'exc':0.0, 'ind':0.0, 'tot':0.0}
    for key, value in dict_parcial.items():
        if 'atividade' in key:
            dict_completo['div'] = dict_parcial[key]
        if 'Consultorias' in key:
            dict_completo['con'] = dict_parcial[key]
        if 'hospedagem' in key:
            dict_completo['loc'] = dict_parcial[key]
        if 'software' in key:
            dict_completo['sof'] = dict_parcial[key]
        if 'expediente' in key:
            dict_completo['exp'] = dict_parcial[key]
        if 'Aluguel' in key:
            dict_completo['imo'] = dict_parcial[key]
        if  'Excedente' in key:
            dict_completo['exc'] = dict_parcial[key]
        if  'indenizado' in key:
            dict_completo['ind'] = dict_parcial[key]
        if 'apresentadas' in key:
            dict_completo['tot'] = dict_parcial[key]

def converte_e_escreve_valores():

    with io.open("dados.csv", 'a', encoding='utf-8') as dados:
        dados.write(deputado + ';' + mes  + ';' + ano + ';')

    for item in dict_completo:
        if type(dict_completo[item]) is unicode:
            dict_completo[item] = str(dict_completo[item])
        if type(dict_completo[item]) is str:
            dict_completo[item] = locale.atof(dict_completo[item])
        #print item, dict_completo[item]
        with open("dados.csv", 'a') as dados:
            if (item != 'con'):
                dados.write(str(dict_completo[item])+ ';')
            else:
                dados.write(str(dict_completo[item]) + '\n')
    print deputado + ' ' +  mes + ' ' + ano


endereco = 'http://www.al.ba.gov.br/deputados/Prestacao-de-Contas.php'
#abre pagina da alba
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)
driver.get(endereco)


while(indice_inicio < tamanho):
    indice = indice_inicio
    loop_deputados(indice,7,5)
    indice_inicio +=1

driver.close()
