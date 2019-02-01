#utf 8
import argparse, requests, bs4, html5lib
from bs4 import BeautifulSoup as BS
parser = argparse.ArgumentParser()

'''
- setar o utf do arquivo e o header de execução do python
- ao rodar o script sem argumentos raspar dados por completo, todos os deputados, todos os anos (perguntar se quer fazer isso antes)
- ao rodar o script com os seguintes argumentos, fazer busca de acordo com os dados passados
    --deputado --ano --mes --categoria
'''
SELETOR = "table.tabela-cab tr.table-itens td"

#http://www.al.ba.gov.br/transparencia/prestacao-contas?categoria=&deputado=903708&mes=3&ano=2018&page=0&size=20
# http://www.al.ba.gov.br/transparencia/prestacao-contas?ano=&categoria=&page=0&size=200
"""
<tr class="table-itens cinza">
    <td width="150">
        <a href="/transparencia/prestacao-contas/34952/">
            <button class="btn fe-btn-alba fe-btn-min-r fe-center-x">
                <i class="fa fa-share-square-o"></i><span>7741</span>
            </button>
        </a>
    </td>
    <td>404</td>
    <td>10/2018</td>
    <td width="150">Aderbal Caldas</td>
    <td>Consultorias</td>
    <td width="150">R$ 6.500,00</td>
</tr>
"""

def base_url(args):
    cat  = args.categoria if args.categoria else ''
    dep  = args.deputado if args.deputado else ''
    ano  = args.ano if args.ano else ''
    mes  = args.mes if args.mes else ''
    base_url = 'http://www.al.ba.gov.br/transparencia/prestacao-contas?categoria={}&deputado={}&mes={}&ano={}&page=0&size=400'.format(cat, dep, mes, ano)
    return base_url
      
def access_page(url):
    page  = requests.get(url)
    source = page.content
    return source

def create_soup(source):
    soup = BS(source, "html5lib")
    return soup

def find_table(soup, seletor):
    table_rows = soup.select(seletor)
    if len(table_rows):
        return table_rows
    else:
        print('Nenhum dado encontrado')
        return False

def iterate_table(soup, table_cels):
    i = 0
    len_tab = len(table_cels)
    print('len_tab')
    print(str(len_tab) + '\n')

    while i < len_tab:               
        processo =  table_cels[0 + i].text
        nf =        table_cels[1 + i].text
        date =      table_cels[2 + i].text
        #ano =       date.split('\\')
        #mes =       date.split('\\')
        dep =       table_cels[3 + i].text
        cat =       table_cels[4 + i].text
        valor =     table_cels[5 + i].text
        print(processo.strip())
        print(nf.strip('0'))
        print(date)
        print(dep)
        print(cat)
        print(valor)
        print('\n')
        i += 6
        
        

if __name__ == "__main__":
    parser.add_argument("-d","--deputado", help="Número do deputado", type=int)
    parser.add_argument("-a","--ano", help="Ano a ser raspado", type=int)
    parser.add_argument("-m","--mes", help="Mês a ser raspado", type=int)
    parser.add_argument("-c","--categoria", help="Categoria a ser raspada", type=int)
    args = parser.parse_args()
    
    url = base_url(args)
    first_source = access_page(url)
    initial_soup = create_soup(first_source)
    table = find_table(initial_soup, SELETOR)

    if(table):
        iterate_table(initial_soup, table)