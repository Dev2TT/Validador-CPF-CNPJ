from flask import Blueprint,jsonify,session,request
from app.services.user_service import UsuarioService
from helpers import autentica_session

usuario_bp=Blueprint('usuario',__name__)

@usuario_bp.route('/usuario/create',methods=['POST'])
def create_usuario():
    try:
        data=request.get_json()
    except Exception as e:
        return jsonify({'message':str(e.args)})
    
    if data:
        try:
            nome=data.get('username')
            senha=data.get('senha')
            usuario=UsuarioService.create_ususario(username=nome,senha=senha)
            
            if usuario == 1:
                return jsonify({'message':'Usuario cadastrado'}),200
            
            return jsonify({'message':usuario})
        except Exception as e:
            return jsonify({'erro':str(e.args)}),400

@usuario_bp.route('/usuario/login',methods=['POST'])
def login():
    try:
        data=request.get_json()
    except Exception as e:
        return jsonify({'erro':str(e.args)})

    if data:
        username=data.get('username')
        senha=data.get('senha')
        logar_usuario=UsuarioService.login(username,senha)
        
        if logar_usuario == 1:
            return jsonify({'message':'Usuario logado'}),200
        if logar_usuario == -1:
            return jsonify({'message':'usuario nao encontrado'}),400

        return jsonify({'message':logar_usuario})
@usuario_bp.route('/usuario/logout',methods=['POST'])
def logout():
    if  autentica_session() == False:
        jsonify({'message':'nao existe usuario logado. Tente acessar a rota "usuario/login"'})
    
    try:
        logout=UsuarioService.logout()
        if logout == 1:
            return jsonify({'message':'logout realizado'}),200
       
        return jsonify({'message':'logout nao realizado'}),400
    except Exception as e:
        return jsonify({'erro':str(e.args)}),400

        
@usuario_bp.route('/usuarios/<int:id_user>',methods=['GET'])
def mostra_usuarios(id_user):
    if  autentica_session() == False:
        jsonify({'message':'nao existe usuario logado. Tente acessar a rota "usuario/login"'})
    
    try:
        usuario=UsuarioService.get_usuario(id_user)
        
        return jsonify({'Usuario':usuario}),200
    
    except Exception as e:
        return jsonify({'erro': usuario}),400


@usuario_bp.route('/usuario',methods=['PUT'])
def atualiza_usuario():
    if autentica_session() == False:
        return jsonify({'message':'nao existe usuario logado. Tente acessar a rota "usuario/login"'})
    
    id_user=session['conta_conectada']

    try:
        data=request.get_json()
        novo_nome=data.get('novo_username')
        nova_senha=data.get('nova_senha')
    except Exception as e:
        return jsonify({'message':str(e.args)})
    
    try:
        usuario=UsuarioService.atualiza_usuario(id_user,novo_nome,nova_senha)
        
        return jsonify({'message':usuario})
    
    except Exception as e:
        return jsonify({'erro':str(e.args)})        


@usuario_bp.route("/usuario",methods=['DELETE'])
def delete_user():
    if autentica_session() == False:
        return jsonify({'message':'nao existe usuario logado. Tente acessar a rota "usuario/login"'})

    id_user=session['conta_conectada']

    try:
        usuario=UsuarioService.delete_usuario(id_user)
        UsuarioService.logout()
        if usuario == 1:
            return jsonify({'message':'usuario apagado'})
        return jsonify({'message':'nao foi possivel deletar o usuario'})
    except Exception as e:
        return jsonify({'message':str(e.args)})
    
    