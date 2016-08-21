
import csv
import json

valor_id = 1000

valor_mes = 0

valor_ano = 2017

i = 1


meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

with open('dados.csv') as arquivo_csv:

	arquivo = open("dados.json", "w")

	arquivo.write('{"deputados": [')

	for line in arquivo_csv:

		linha = line.split(";")
	

		if int(linha[1]) != valor_id:
			#arquivo.write('"nome": "' + linha[0] + '",')
			#arquivo.write("ano":{' + '"' + linha[3] +'":{'')
			if int(linha[1]) == 1001:
				arquivo.write('{')
			else:
				arquivo.write(',{')
			arquivo.write('"nome": "' + linha[0] + '",')
			arquivo.write('"id": "' + linha[1] + '",')
			arquivo.write('"ano":{')
			valor_id = valor_id + 1
			valor_ano = 2017

		if int(linha[3]) != valor_ano:
			#arquivo.write('"ano":{' + '"' + linha[3] +'":{')
			arquivo.write('"' + linha[3] +'":{')
			valor_ano = valor_ano - 1
			arquivo.write('"' + linha[2] + '":{' )
			arquivo.write('"loc": "'+ linha[4] +'",')
			arquivo.write('"tot": "'+ linha[5] +'",')
			arquivo.write('"exc": "'+ linha[6] +'",')
			arquivo.write('"exp": "'+ linha[7] +'",')
			arquivo.write('"sof": "'+ linha[8] +'",')
			arquivo.write('"ind": "'+ linha[9] +'",')
			arquivo.write('"div": "'+ linha[10] +'",')
			arquivo.write('"imo": "'+ linha[11] +'",')
			arquivo.write('"con": "'+ linha[12].rstrip() + '"' +'},')

		else:
			for mes in meses:
				if mes == linha[2]:
					arquivo.write('"' + linha[2] + '":{')
					arquivo.write('"loc": "'+ linha[4] +'",')
					arquivo.write('"tot": "'+ linha[5] +'",')
					arquivo.write('"exc": "'+ linha[6] +'",')
					arquivo.write('"exp": "'+ linha[7] +'",')
					arquivo.write('"sof": "'+ linha[8] +'",')
					arquivo.write('"ind": "'+ linha[9] +'",')
					arquivo.write('"div": "'+ linha[10] +'",')
					arquivo.write('"imo": "'+ linha[11] +'",')
					if linha[2] != 'dez':
						arquivo.write('"con": "'+ linha[12].rstrip() + '"' +'},')
					else:
						arquivo.write('"con": "'+ linha[12].rstrip() + '"' +'}')
						if linha[3] != '2008':
							arquivo.write('},')
						else:
							arquivo.write('}')
							arquivo.write('}')
		
		if linha[3] == '2008' and linha[2] == 'dez':
			arquivo.write('}')
#deputado;id;mes;ano;loc;tot;exc;exp;sof;ind;div;imo;con


		#arquivo.write(str(i))
		#arquivo.write(str(i))
		i = i + 1

arquivo.write(']}')
