import ConexaoBD as bd

def GetListAreaPreservacaoPermante():
  lista = bd.GetListAPP()
  resposta = {'IsSuccess':'true',
             'data':lista,
             'message':'null'}
  return resposta

  
def GetFiltroAreaPreservacaoPermante():
  dado = bd.GetFiltroAPP()
  resposta = {'IsSuccess':'true',
             'data':dado,
             'message':'null'}
  return resposta