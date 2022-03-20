import ConexaoBD as bd

def GetListImovelRural():
  lista = bd.GetListIR()
  resposta = {'IsSuccess':'true',
             'data':lista,
             'message':'null'}
  return resposta

  
def GetFiltroImovelRural():
  dado = bd.GetFiltroIR()
  resposta = {'IsSuccess':'true',
             'data':dado,
             'message':'null'}
  return resposta

