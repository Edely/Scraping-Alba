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
SELETOR = "table.tabela-cab .table-itens"

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
    print(url)
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

def iterate_table(soup, table_rows):
    for row in table_rows:       
        tds = soup.find_all('td')
        #for td in tds:
        date = ''
        mes = ''
        ano = ''
        data = ''
        #    print('================')
        #    print('======AQUI======')
        #    print('================')
        #    print(td)
        break  
        

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
    iterate_table(initial_soup, table)