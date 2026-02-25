from flask import session
from extensions import db
from app.models.usuarios import Usuario

class UsuarioService:
    @staticmethod
    def login(username:str,senha:str):
        try:
            query=db.session.execute(db.Query(Usuario).filter_by(username=username)).scalar()
        except Exception as e:
            return str(e.args)

        if query:
            if query.username == username:
                if query.senha == senha:
                    if 'conta_conectada' not in session or session['conta_conectada'] == None:
                        session['conta_conectada'] = query.id_usuario
                        return 1
                    return f'conta com id {session['conta_conectada']} ja esta logada'
        return -1
    @staticmethod
    def logout():
        if 'conta_conectada' in session and session['conta_conectada'] != None:
            session['conta_conectada']=None
            return 1
        
        return -1
    
    @staticmethod
    def create_ususario(username:str,senha:str):
        if username == None or username == '':
            return 'credencial {username} invalida'
        if senha == None or senha == '':
            return 'credencial {senha} invalida'
        
        usuario=Usuario(
            username=username,
            senha=senha
        )

        try:
            db.session.add(usuario)
            db.session.commit()
            return 1
        except Exception as e:
            return str(e.args)
        

    @staticmethod
    def get_usuario(id):
        try:
            query=db.session.execute(db.Query(Usuario).filter_by(id_usuario=id)).scalar()
            return {'nome':query.username,'senha':query.senha}
        except Exception as e:
            return str(e.args)
        
    
    @staticmethod
    def atualiza_usuario(id_user:int, novo_nome:str, nova_senha:str):
        try:
            query=db.session.execute(db.Query(Usuario).filter_by(id_usuario=id_user)).scalar()
        except Exception as e:
            return str(e.args)
        
        if query:
            if query.username != novo_nome:
                query.username=novo_nome
            if query.senha != nova_senha:
                query.senha=nova_senha
            
            db.session.commit()

            return 'atualizado'
        return 'nao atualizado'

    @staticmethod
    def delete_usuario(id_user):
        try:
            query=db.session.execute(db.Query(Usuario).filter_by(id_usuario=id_user)).scalar()
        except Exception as e:
            return str(e.args)

        if query:
            db.session.delete(query)
            db.session.commit()
            return 1
        

        return -1
