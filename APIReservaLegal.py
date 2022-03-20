import ConexaoBD as bd

def GetListReservaLegal():
  lista = bd.GetListRL()
  resposta = {'IsSuccess':'true',
             'data':lista,
             'message':'null'}
  return resposta

  
def GetFiltroReservaLegal():
  dado = bd.GetFiltroRL()
  resposta = {'IsSuccess':'true',
             'data':dado,
             'message':'null'}
  return resposta
