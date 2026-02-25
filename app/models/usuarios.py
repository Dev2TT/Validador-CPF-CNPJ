from extensions import db

class Usuario(db.Model):
    id_usuario= db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(50), nullable=False)
    senha=db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f'[Nome: {self.username}\nSenha: {self.senha}]'

    