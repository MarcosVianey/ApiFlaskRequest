from enum import unique
from db import db

class CadastroModel(db.Model):
    __tablename__ = 'cadastros'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    telefone = db.Column(db.Integer, nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, telefone, idade):
        self.nome = nome
        self.telefone = telefone
        self.idade = idade

    def __repr__(self, ):
        return f'Cadastro(nome={self.nome}, idade={self.idade}, telefone={self.telefone})'

    def json(self, ):
         return{
             'nome': self.nome,
             'idade': self.idade,
             'telefone': self.telefone
         }

    @classmethod
    def find_by_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

