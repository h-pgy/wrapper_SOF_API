import pandas as pd
import requests
import json


class RequisicaoApi():

    def __aux_dict_consulta(self, dict_consulta):

        consulta = []

        if dict_consulta:
            for key, value in dict_consulta.items():
                consulta.append('='.join([str(key), str(value)]))

            return '&'.join(consulta)
        else:
            return ''

    def __requisicao(self, num_pag, consulta, dict_consulta = ''):

        num_pag = str(num_pag)
        if dict_consulta:
                consulta = ''.join([consulta, '?', self.__aux_dict_consulta(dict_consulta)])

        url_base = r'https://gatewayapi.prodam.sp.gov.br:443/financas/orcamento/sof/v2.1.0/{}'.format(consulta)
        if dict_consulta:
            url = url_base + '&numPagina=' + num_pag
        else:
            url = url_base + '?numPagina' + num_pag
        # proxies = {'https' : 'https://USUARIO:SENHA@DOMINIO:PORTA'} configure essa variavel para usar o proxy e coloque o param abaixo
        headers = {
        "user-agent": "Mozilla/5za.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
        "Authorization": "Bearer e313743a132ccc6c68a46e91c29f"
            }

        token = 'e313743a132ccc6c68a46e91c29f'
        
        with requests.get(url, headers = headers) as r: # acrescente o param proxies = proxies para usar proxy

            dados = r.json()
                
        return dados

    def __formater_csv(self, dados, key_dados):
        
        if dados['metadados']['txtStatus'] == 'ERRO':
            return dados['metadados']['txtMensagemErro']
        
        else:

            valores = [c for c in dados[key_dados]]
            dic_dados = {coluna : [] for coluna in list(valores[0].keys())}

            for valor in valores:
                for key, value in valor.items():
                    value = str(value)
                    value = value.replace('\n', ' ')
                    value = value.replace(';', ',')
                    value = value.replace('\r', ' ')
                    dic_dados[key].append(value)

            return dic_dados
        
    def __aux_csv_writer(self, colunas, dados_requisi, key_dados, consulta):
        
        dici = self.__formater_csv(dados_requisi, key_dados)
        
        with open('dados_{}.csv'.format(consulta), 'a') as f:
            
            for col in colunas:
                for z in range(len(dici[colunas[0]])):
                    line = [str(dici[col][z]) for col in colunas]
                    f.write(';'.join(line) + '\n')
                
                                 

    def puxar_todos_valores(self, key_dados, consulta, dict_consulta, csv = False):
        
        dados = []
        
        primeira_requisicao = self.__requisicao(1, consulta, dict_consulta)
        qtd_paginas = primeira_requisicao['metadados']['qtdPaginas']
        print('O total de paginas é :::' + str(qtd_paginas))
        
        if csv:
            
            colunas = [str(coluna) for coluna in list(primeira_requisicao[key_dados][0].keys())]
            
            with open('dados_{}.csv'.format(consulta), 'w') as f:
                f.write(';'.join(colunas) + '\n')
            
        for i in range(1, qtd_paginas + 1):

            dados_requisi = self.__requisicao(i, consulta, dict_consulta)
            if dados_requisi['metadados']['txtStatus'] == 'ERRO':
                print('ERRO - pagina {pg} - txt erro :: {erro}'.format(pg = i, erro = dados_requisi['metadados']['txtMensagemErro']))
            else:
                dados.append(dados_requisi[key_dados])
                if csv:
                    self.__aux_csv_writer(colunas, dados_requisi, key_dados, consulta)
                    
        dados = [dic_ for lista in dados for dic_ in lista]

        return pd.DataFrame(dados)
            
            


