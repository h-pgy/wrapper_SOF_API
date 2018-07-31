# wrapper_SOF_API
 wapper em python para a API do SOF (Sistema Orçamentário financeiro da Prefeitura Municipal de São Paulo). Parseia os jsons e gera dataframes e/ou .csvs para cada consulta disponível na API
 
 
## modulo = superclasse_api

Contém a superclasse que abstrai as consultas à API, parseia os Jsons gerando DataFrames e que inclui a possibilidade de criar .csvs que são escritos de formas incremental, linha por linha, conforme as requisições à API vão sendo realizadas (é útil para consultas muito grandes, para evitar estouro de memória e/ou perda dos dados devido a um possível erro na requisição).

## modulo = consultas_api

Contém as classes herdeiras da superclasse que replicam todas as consultas que podem ser realizadas à API, assim como seus respectivos parâmetros obrigatórios e opcionais
