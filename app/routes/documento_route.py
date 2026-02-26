from flask import Blueprint, jsonify
from helpers import autentica_session,verifica_cpf,verifica_cnpj
from app.services.documento_service import DocumentoService

documento_bp=Blueprint('documento', __name__)

@documento_bp.route('/documento/cpf/<string:cpf>',methods=['POST'])
def valida_cpf(cpf):
    if autentica_session() == False:
        return jsonify({'message':'usuario nao logado. Tente a rota "/usuario/login"!'}),400
    try:
        if verifica_cpf(cpf) == False:
            return jsonify({'message':'cpf invalido'}),400
        return jsonify({'message':'CPF valido'}),200
    except Exception as e:
        return jsonify({'erro':str(e.args)}),400


@documento_bp.route('/documento/cnpj/<string:cnpj>',methods=['POST'])
def consulta_cnpj(cnpj:str):
    if autentica_session() == False:
        return jsonify({'message':'usuario nao logado. Tente acessar a [/usuario/login]'}),400
    
    if verifica_cnpj(cnpj) == False:
        return jsonify({'message':'cnpj invalido'}),200
    
    try:
        request=DocumentoService.puxa_cnpj(cnpj)
        
        if request == False:
            return jsonify({'message':'CNPJ nao encontrado'})
        
        dados={
            'CNPJ':request['cnpj'],
            'Razao Social':request['razao_social'],
            'Nome Fantasia':request['nome_fantasia'],
            'Situacao Cadastral':request['situacao_cadastral'],
            'Data de Inicio':request['data_inicio_atividade']
        }

        return jsonify(dados)

    except Exception as e:
        return jsonify({'erro':str(e.args)}),400