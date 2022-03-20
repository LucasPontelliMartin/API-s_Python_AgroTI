import pandas as pd;

def GetListIR():
  retorno = {'CODIGO_DO_IMOVEL':'190014738','DENOMINACAO_DO_IMOVEL':'Colonia Iracema','CODIGO_DO_MUNICIPIO (IBGE)':'1200013','area':'71,8309','UF':'AC',
'municipio':'ACRELANDIA','TITULAR':'MARIA ********************', 'CONDICAO_DA_PESSOA':'Proprietario Ou Posseiro Individual','PERCENTUAL_DE_DETENCAO':'100'},{'CODIGO_DO_IMOVEL':'190020975','DENOMINACAO_DO_IMOVEL':'COLONIA BOA ESPERANCA','CODIGO_DO_MUNICIPIO (IBGE)':'1200013','area':'59,7018','UF':'AC',
'municipio':'ACRELANDIA','TITULAR':'PERCIVAL ********************', 'CONDICAO_DA_PESSOA':'Proprietario Ou Posseiro Individual','PERCENTUAL_DE_DETENCAO':'100'},{'CODIGO_DO_IMOVEL':'190025004','DENOMINACAO_DO_IMOVEL':'Colonia Sauval','CODIGO_DO_MUNICIPIO (IBGE)':'1200013','area':'41,4','UF':'AC',
'municipio':'ACRELANDIA','TITULAR':'ARTIDOR ********************', 'CONDICAO_DA_PESSOA':'Proprietario Ou Posseiro Individual','PERCENTUAL_DE_DETENCAO':'100'},{'CODIGO_DO_IMOVEL':'190036111','DENOMINACAO_DO_IMOVEL':'Colonia M C','CODIGO_DO_MUNICIPIO (IBGE)':'1200013','area':'15','UF':'AC',
'municipio':'ACRELANDIA','TITULAR':'JIMIM ********************', 'CONDICAO_DA_PESSOA':'Proprietario Ou Posseiro Individual','PERCENTUAL_DE_DETENCAO':'100'},{'CODIGO_DO_IMOVEL':'190036383','DENOMINACAO_DO_IMOVEL':'Colonia Tres Nascentes','CODIGO_DO_MUNICIPIO (IBGE)':'1200013','area':'78,8483','UF':'AC',
'municipio':'ACRELANDIA','TITULAR':'MARIA ********************', 'CONDICAO_DA_PESSOA':'Proprietario Ou Posseiro Individual','PERCENTUAL_DE_DETENCAO':'100'}
  return retorno

def GetFiltroIR():
  retorno = {'CODIGO_DO_IMOVEL':'190020975','DENOMINACAO_DO_IMOVEL':'COLONIA BOA ESPERANCA','CODIGO_DO_MUNICIPIO (IBGE)':'1200013','area':'59,7018','UF':'AC',
'municipio':'ACRELANDIA','TITULAR':'PERCIVAL ********************', 'CONDICAO_DA_PESSOA':'Proprietario Ou Posseiro Individual','PERCENTUAL_DE_DETENCAO':'100'}
  return retorno

def GetListAPP():
  retorno = {'IDF':'391048','NOM_TEMA':'Area de Preservacao Permanente de Nascentes ou Olhos Agua Perenes', 'NUM_AREA':'0.785082763671875'},{'IDF':'396340','NOM_TEMA':'Area de Preservacao Permanente de Rios ate 10 metros', 'NUM_AREA':'0.288382250976563'},{'IDF':'402927','NOM_TEMA':'Area de Preservacao Permanente de Rios ate 10 metros', 'NUM_AREA':'0.643761328125'},{'IDF':'416830','NOM_TEMA':'Area de Preservacao Permanente de Rios ate 10 metros', 'NUM_AREA':'7.66297734375'},{'IDF':'421974','NOM_TEMA':'Area de Preservacao Permanente de Reservatorio artificial decorrente de barramento de cursos dagua', 'NUM_AREA':'0.313691198825836'}
  return retorno

def GetFiltroAPP():
  retorno = {'IDF':'421974','NOM_TEMA':'Area de Preservacao Permanente de Reservatorio artificial decorrente de barramento de cursos dagua', 'NUM_AREA':'0.313691198825836'}
  return retorno

def GetListRL():
  retorno = {'IDF':'417532','NOM_TEMA':'Reserva Legal Proposta', 'NUM_AREA':'1.9133919921875'},{'IDF':'422141','NOM_TEMA':'Reserva Legal Proposta', 'NUM_AREA':'0.111175246536732'},{'IDF':'447107','NOM_TEMA':'Reserva Legal Proposta', 'NUM_AREA':'0.441095703125'},{'IDF':'447238','NOM_TEMA':'Reserva Legal Proposta', 'NUM_AREA':'0.9401267578125'},{'IDF':'494013','NOM_TEMA':'Reserva Legal Proposta', 'NUM_AREA':'1.1497390625'},{'IDF':'603097','NOM_TEMA':'Reserva Legal Proposta', 'NUM_AREA':'2.8721953125'}
  return retorno


def GetFiltroRL():
  retorno = {'IDF':'447238','NOM_TEMA':'Reserva Legal Proposta', 'NUM_AREA':'0.9401267578125'}
  return retorno