from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Funcionario(UserMixin, db.Model):
    """
    Criar a tabela empregados
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    usuario = db.Column(db.String(60), index=True, unique=True)
    primeiro_nome = db.Column(db.String(60), index=True)
    ultimo_nome = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('Senha nao e um atributo legivel')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, senha):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, senha)

    def __repr__(self):
        return '<Funcionario: {}>'.format(self.usuario)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Funcionario.query.get(int(user_id))


class Noticia(db.Model):
    """
    Criar tabela noticias
    """

    __tablename__ = 'noticias'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(60), unique=True)
    caminho_imagem = db.Column(db.String(100))
    texto = db.Column(db.String(3000))

    def __repr__(self):
        return '<Titulo: {}>'.format(self.titulo)