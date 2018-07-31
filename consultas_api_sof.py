import pandas as pd
import requests
import json

from superclasse_api_sof import RequisicaoApi

class Credores(RequisicaoApi):
    
    def __init__(self, cpf = '', cnpj = '', razao_social = '', nome_fantasia = '', tipo_fornecedor = '', csv = False):
        
        self.consulta = 'consultarCredores'
        self.key_dados = 'lstCredores'
        self.csv = csv
        
        self.dict_consulta = {}
    
        if cpf:
            self.dict_consulta['numCpfCnpj'] = cpf
        
        if cnpj:
            self.dict_consulta['numCpfCnpj'] = cnpj
            
        if razao_social:
            self.dict_consulta['txtRazaoSocial'] = razao_social
        
        if nome_fantasia:
            self.dict_consulta['nomFanstasia'] = nome_fantasia
        
        if tipo_fornecedor:
            self.dict_consulta['txtTipoFornecedor'] = tipo_fornecedor
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        

class Modalidades(RequisicaoApi):
    
    
    def __init__(self, ano, categoria = '', modalidade = '', grupo = '', csv = False):
        
        self.consulta = 'consultarModalidades'
        self.key_dados = 'lstModalidades'
        self.csv = csv

        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
    
        if categoria:
            self.dict_consulta['codCategoria'] = categoria
        
        if modalidade:
            self.dict_consulta['codModalidade'] = modalidade
            
        if grupo:
            self.dict_consulta['codGrupo'] = razao_social
        
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        

class ContasReceita(RequisicaoApi):
    
    
    def __init__(self, ano, cod_receita = '',csv = False):
        
        self.consulta = 'consultarContasReceita'
        self.key_dados = 'lstReceita'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
    
        if cod_receita:
            self.dict_consulta['codReceita'] = cod_receita
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Funcoes(RequisicaoApi):
    
    
    def __init__(self, ano, cod_funcao = '',csv = False):
        
        self.consulta = 'consultarFuncoes'
        self.key_dados = 'lstFuncoes'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
    
        if cod_funcao:
            self.dict_consulta['codFuncao'] = cod_funcao
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        

class Contratos(RequisicaoApi):
    
    def __init__(self, cod_contrato = '', ano = '', cpf = '', cod_empresa = '', cod_orgao = '', csv = False):
        
        self.consulta = 'consultaContrato'
        self.key_dados = 'lstContratos'
        self.csv = csv
        
        self.dict_consulta = {}
    
        if cod_contrato:
            self.dict_consulta['codContrato'] = cod_contrato
        if ano:
            self.dict_consulta['anoContrato'] = ano
        if cpf:
            self.dict_consulta['numCpfCnpj'] = cpf
        if cod_empresa:
            self.dict_consulta['codEmpresa'] = cod_empresa
        if cod_orgao:
            self.dict_consulta['codOrgao'] = cod_orgao
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        

class Elementos(RequisicaoApi):
    
    def __init__(self, ano, cod_categoria = '', cod_grupo = '', cod_modalidade = '', cod_elemento = '', csv = False):
        
        self.consulta = 'consultarElementos'
        self.key_dados = 'lstElementos'
        self.csv = csv
        
        self.dict_consulta = {}
                 
        self.dict_consulta['anoExercicio'] = ano
    
        if cod_categoria:
            self.dict_consulta['codCategoria'] = cod_categoria
        
        if cod_grupo:
            self.dict_consulta['codGrupo'] = cod_grupo
            
        if cod_modalidade:
            self.dict_consulta['codModalidade'] = cod_modalidade
        
        if cod_elemento:
            self.dict_consulta['codElemento'] = cod_elemento
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)

        
class Grupos(RequisicaoApi):
    
    def __init__(self, ano, cod_categoria = '', cod_grupo = '', csv = False):
        
        self.consulta = 'consultarGrupos'
        self.key_dados = 'lstGrupos'
        self.csv = csv
        
        self.dict_consulta = {}
                 
        self.dict_consulta['anoExercicio'] = ano
    
        if cod_categoria:
            self.dict_consulta['codCategoria'] = cod_categoria
        
        if cod_grupo:
            self.dict_consulta['codGrupo'] = cod_grupo
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Categorias(RequisicaoApi):
    
    def __init__(self, ano, cod_categoria = '', csv = False):
        
        self.consulta = 'consultarCategorias'
        self.key_dados = 'lstCategorias'
        self.csv = csv
        
        self.dict_consulta = {}
                 
        self.dict_consulta['anoExercicio'] = ano
    
        if cod_categoria:
            self.dict_consulta['codCategoria'] = cod_categoria
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Empenhos(RequisicaoApi):
    
    def __init__(self, ano, mes, cod_empenho = '', cod_empresa = '', cpf = '', cnpj = '', razao_social = '', cod_contrato = '', ano_contrato = '', cod_orgao = '', cod_unidade = '', funcao = '', subfuncao = '', projeto_atividade = '', programa = '',  categoria = '', grupo = '', modalidade = '', elemento = '', fonte = '', item_despesa = '',  subelemento = '', csv = False):
        
        self.consulta = 'consultaEmpenhos'
        self.key_dados = 'lstEmpenhos'
        self.csv = csv
        
        self.dict_consulta = {}
                 
        self.dict_consulta['anoExercicio'] = ano
        self.dict_consulta['mesEmpenho'] = mes

        if cod_empenho:
            self.dict_consulta['codEmpenho'] = cod_empenho
        if cod_empresa:
            self.dict_consulta['codEmpresa'] = cod_empresa
        if cpf:
            self.dict_consulta['numCpfCnpj'] = cpf
        if cnpj:
            self.dict_consulta['numCpfCnpj'] = cnpj
        if razao_social:
            self.dict_consulta['txtRazaoSocial'] = razao_social
        if cod_contrato:
            self.dict_consulta['codContrato'] = cod_contrato
        if ano_contrato:
            self.dict_consulta['anoExercicio'] = ano_contrato
        if cod_orgao:
            self.dict_consulta['codOrgao'] = cod_orgao
        if cod_unidade:
            self.dict_consulta['codUnidade'] = cod_unidade
        if funcao:
            self.dict_consulta['codFuncao'] = funcao
        if subfuncao:
            self.dict_consulta['codSubFuncao'] = subfuncao
        if projeto_atividade:
            self.dict_consulta['codProjetoAtividade'] = projeto_atividade
        if programa:
            self.dict_consulta['codPrograma'] = programa
        if categoria:
            self.dict_consulta['codCategoria'] = categoria
        if grupo:
            self.dict_consulta['codGrupo'] = grupo
        if modalidade:
            self.dict_consulta['codModalidade'] = modalidade
        if elemento:
            self.dict_consulta['codElemento'] = elemento
        if fonte:
            self.dict_consulta['codFonteRecurso'] = fonte
        if item_despesa:
            self.dict_consulta['codItemDespesa'] = item_despesa
        if subelemento:
            self.dict_consulta['codSubElemento'] = subelemento
        
        
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class CredoresdeContrato(RequisicaoApi):
    
    def __init__(self, ano, cod_contrato, cod_empresa, csv = False):
        
        self.consulta = 'consultarCredoresDeContrato'
        self.key_dados = 'lstCredoresDeContrato'
        self.csv = csv
        
        self.dict_consulta = {}
                 
        self.dict_consulta['anoExercicio'] = ano
        self.dict_consulta['codContrato'] = cod_contrato
        self.dict_consulta['codEmpresa'] = cod_empresa

            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class SubElementos(RequisicaoApi):
    
    def __init__(self, ano, categoria, grupo, modalidade, elemento, subelemento ='',  csv = False):
        
        self.consulta = 'consultarSubElementos'
        self.key_dados = 'lstSubElementos'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        self.dict_consulta['codCategoria'] = categoria
        self.dict_consulta['codGrupo'] = grupo
        self.dict_consulta['codModalidade'] = modalidade
        self.dict_consulta['codElemento'] = elemento
        
        if subelemento:
            self.dict_consulta['codSubElemento'] = subelemento

            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Programas(RequisicaoApi):
    
    def __init__(self, ano, programa = '', csv = False):
        
        self.consulta = 'consultarProgramas'
        self.key_dados = 'lstProgramas'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        
        if programa:
            self.dict_consulta['codPrograma'] = programa
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class MovimentosReceita(RequisicaoApi):
    
    def __init__(self, ano, mes = '', cod_receita = '', empresa = '', csv = False):
        
        self.consulta = 'consultarMovimentosReceita'
        self.key_dados = 'lstMonvimentosReceita'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        
        if cod_receita:
            self.dict_consulta['codReceita'] = cod_receita
        if mes:
            self.dict_consulta['mesAteMovimento'] = mes
        if empresa:
            self.dict_consulta['codEmpresa'] = empresa
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
class FonteRecursos(RequisicaoApi):
    
    def __init__(self, ano, cod_fonte = '', csv = False):
        
        self.consulta = 'consultarFonteRecursos'
        self.key_dados = 'lstFontesRecursos'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        
        if cod_fonte:
            self.dict_consulta['codFonteRecurso'] = cod_fonte
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class ProjetosAtividades(RequisicaoApi):
    
    def __init__(self, ano, cod_projeto_atividade = '', csv = False):
        
        self.consulta = 'consultarProjetosAtividades'
        self.key_dados = 'lstProjetosAtividades'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        
        if cod_projeto_atividade:
            self.dict_consulta['codProjetoAtividade'] = cod_projeto_atividade
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Empresas(RequisicaoApi):
    
    def __init__(self, ano, cod_empresa = '', csv = False):
        
        self.consulta = 'consultarEmpresas'
        self.key_dados = 'lstEmpresas'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        
        if cod_empresa:
            self.dict_consulta['codEmpresa'] = cod_empresa
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Empresas(RequisicaoApi):
    
    def __init__(self, ano, cod_subfuncao = '', csv = False):
        
        self.consulta = 'consultarSubFuncoes'
        self.key_dados = 'lstSubFuncoes'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        
        if cod_subfuncao:
            self.dict_consulta['codSubFuncao'] = cod_subfuncao
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Liquidacoes(RequisicaoApi):
    
    def __init__(self, ano_empenho, cod_empenho, cod_empresa, csv = False):
        
        self.consulta = 'consultarLiquidacoes'
        self.key_dados = 'lstLiquidacoes'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoEmpenho'] = ano_empenho
        self.dict_consulta['codEmpenho'] = cod_empenho
        self.dict_consulta['codEmpresa'] = cod_empresa

            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Orgaos(RequisicaoApi):
    
    def __init__(self, ano, cod_orgao = '', cod_empresa = '', csv = False):
        
        self.consulta = 'consultarOrgaos'
        self.key_dados = 'lstOrgaos'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        
        if cod_orgao:
            self.dict_consulta['codOrgao'] = cod_orgao
        if cod_empresa:
            self.dict_consulta['codEmpresa'] = cod_empresa
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class DespesasCredor(RequisicaoApi):
    
    def __init__(self, ano, mes, cpf = '', cnpj = '', razao_social = '', cod_empresa = '', cod_orgao = '', cod_unidade = '', funcao = '', subfuncao = '', projeto_atividade = '', programa = '',  categoria = '', grupo = '', modalidade = '', elemento = '', fonte = '', item_despesa = '',  subelemento = '', csv = False):
        
        self.consulta = 'consultarDespesasCredor'
        self.key_dados = 'lstCredores'
        self.csv = csv
        
        self.dict_consulta = {}
                 
        self.dict_consulta['anoExercicio'] = ano
        self.dict_consulta['mesEmpenho'] = mes

        if cpf:
            self.dict_consulta['numCpfCnpj'] = cpf
        if cnpj:
            self.dict_consulta['numCpfCnpj'] = cnpj
        if razao_social:
            self.dict_consulta['txtRazaoSocial'] = razao_social
        if cod_empresa:
            self.dict_consulta['codEmpresa'] = cod_empresa
        if cod_orgao:
            self.dict_consulta['codOrgao'] = cod_orgao
        if cod_unidade:
            self.dict_consulta['codUnidade'] = cod_unidade
        if funcao:
            self.dict_consulta['codFuncao'] = funcao
        if subfuncao:
            self.dict_consulta['codSubFuncao'] = subfuncao
        if projeto_atividade:
            self.dict_consulta['codProjetoAtividade'] = projeto_atividade
        if programa:
            self.dict_consulta['codPrograma'] = programa
        if categoria:
            self.dict_consulta['codCategoria'] = categoria
        if grupo:
            self.dict_consulta['codGrupo'] = grupo
        if modalidade:
            self.dict_consulta['codModalidade'] = modalidade
        if elemento:
            self.dict_consulta['codElemento'] = elemento
        if fonte:
            self.dict_consulta['codFonteRecurso'] = fonte
        if item_despesa:
            self.dict_consulta['codItemDespesa'] = item_despesa
        if subelemento:
            self.dict_consulta['codSubElemento'] = subelemento
        
        
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        

class ItensDespesa(RequisicaoApi):
    
    def __init__(self, ano,  categoria = '', grupo = '', modalidade = '', elemento = '', item_despesa = '',  subelemento = '', csv = False):
        
        self.consulta = 'consultarItensDespesa'
        self.key_dados = 'lstItensDespesa'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano

        if categoria:
            self.dict_consulta['codCategoria'] = categoria
        if grupo:
            self.dict_consulta['codGrupo'] = grupo
        if modalidade:
            self.dict_consulta['codModalidade'] = modalidade
        if elemento:
            self.dict_consulta['codElemento'] = elemento
        if item_despesa:
            self.dict_consulta['codItemDespesa'] = item_despesa
        if subelemento:
            self.dict_consulta['codSubElemento'] = subelemento
        
        
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)      
        
        
class Unidades(RequisicaoApi):
    
    def __init__(self, ano, cod_orgao, cod_unidade = '', csv = False):
        
        self.consulta = 'consultarUnidades'
        self.key_dados = 'lstUnidades'
        self.csv = csv
        
        self.dict_consulta = {}
        
        self.dict_consulta['anoExercicio'] = ano
        self.dict_consulta['codOrgao'] = cod_orgao

        if cod_unidade:
            self.dict_consulta['codUnidade'] = cod_unidade
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)
        
        
class Despesas(RequisicaoApi):
    
    def __init__(self, ano_dotacao, mes_dotacao, cod_empresa = '', cod_orgao = '', cod_unidade = '', funcao = '', subfuncao = '', projeto_atividade = '', programa = '',  categoria = '', grupo = '', modalidade = '', elemento = '', fonte = '', csv = False):
        
        self.consulta = 'consultarDespesasCredor'
        self.key_dados = 'lstCredores'
        self.csv = csv
        
        self.dict_consulta = {}
                 
        self.dict_consulta['anoDotacao'] = ano_dotacao
        self.dict_consulta['mesDotacao'] = mes_dotacao

        if cod_empresa:
            self.dict_consulta['codEmpresa'] = cod_empresa
        if cod_orgao:
            self.dict_consulta['codOrgao'] = cod_orgao
        if cod_unidade:
            self.dict_consulta['codUnidade'] = cod_unidade
        if funcao:
            self.dict_consulta['codFuncao'] = funcao
        if subfuncao:
            self.dict_consulta['codSubFuncao'] = subfuncao
        if projeto_atividade:
            self.dict_consulta['codProjetoAtividade'] = projeto_atividade
        if programa:
            self.dict_consulta['codPrograma'] = programa
        if categoria:
            self.dict_consulta['codCategoria'] = categoria
        if grupo:
            self.dict_consulta['codGrupo'] = grupo
        if modalidade:
            self.dict_consulta['codModalidade'] = modalidade
        if elemento:
            self.dict_consulta['codElemento'] = elemento
        if fonte:
            self.dict_consulta['codFonteRecurso'] = fonte
        
            
        self.dados = self.puxar_todos_valores(self.key_dados, self.consulta, self.dict_consulta, self.csv)

        

        

        

        
        

        

        

        
        

            
            