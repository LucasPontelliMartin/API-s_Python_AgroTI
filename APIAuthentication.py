def ValidarUsuario():
  valido = 'true'
  return valido

def UsuarioInvalido():
  resposta = {'IsSuccess':'true',
             'data':'null',
             'message':'Voce nao tem permissao para esta acao'}
  return resposta
