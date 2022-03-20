import pandas as pd;
from flask import Flask, jsonify

import APIImovelRural as IR
import APIAreaPreservacaoPermantente as APP
import APIReservaLegal as RL
import APIPing as Ping
import APIAuthentication as Authentication

app = Flask(__name__)

@app.route('/ping')
def homepage():
  resposta = Ping.GetPing()
  return jsonify(resposta)

@app.route('/ListarImovelRural')
def ListarImovelRural():
  resposta = 'null'
  if(Authentication.ValidarUsuario() == 'true'):
    resposta = IR.GetListImovelRural()
  else:
    resposta = Authentication.UsuarioInvalido()
  
  return jsonify(resposta)


@app.route('/ImovelRural/<int:id>', methods=['GET'])
def ImovelRural(id):
  resposta = 'null'
  if(Authentication.ValidarUsuario() == 'true'):
    resposta = IR.GetFiltroImovelRural()
  else:
    resposta = Authentication.UsuarioInvalido()
  
  return jsonify(resposta)


@app.route('/ListarAreaPreservacaoPermantente')
def ListarAreaPreservacaoPermantente():
  resposta = 'null'
  if(Authentication.ValidarUsuario() == 'true'):
    resposta = APP.GetListAreaPreservacaoPermante()
  else:
    resposta = Authentication.UsuarioInvalido()
  
  return jsonify(resposta)


@app.route('/AreaPreservacaoPermantente/<int:id>', methods=['GET'])
def AreaPreservacaoPermantente(id):
  resposta = 'null'
  if(Authentication.ValidarUsuario() == 'true'):
    resposta = APP.GetFiltroAreaPreservacaoPermante()
  else:
    resposta = Authentication.UsuarioInvalido()
  
  return jsonify(resposta)


@app.route('/ListarReservaLegal')
def ListarReservaLegal():
  resposta = 'null'
  if(Authentication.ValidarUsuario() == 'true'):
    resposta = RL.GetListReservaLegal()
  else:
    resposta = Authentication.UsuarioInvalido()
  
  return jsonify(resposta)


@app.route('/ReservaLegal/<int:id>', methods=['GET'])
def ReservaLegal(id):
  resposta = 'null'
  if(Authentication.ValidarUsuario() == 'true'):
    resposta = RL.GetFiltroReservaLegal()
  else:
    resposta = Authentication.UsuarioInvalido()
  return jsonify(resposta)

  
app.run(host='0.0.0.0')

