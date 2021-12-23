from flask import request
from flask_restplus import Resource, fields

from models.cadastro import CadastroModel
from schemas.cadastro import CadastroSchema

from server.instance import server

cadastro_ns = server.cadastro_ns
cadastro_schema = CadastroSchema()
cadastro_list_schema = CadastroSchema(many=True)

NAO_POSSUI_CADASTRO = 'Não Possui Cadastro'

item = cadastro_ns.model('Cadastro', {
    'nome': fields.String(description='Nome Completo'),
    'idade': fields.Integer(description ='Informe Sua Idade'),
    'telefone': fields.Integer(description='Informe Seu Telefone')  
})

class Cadastro(Resource):

    def get(self, id):
        cadastro_data = CadastroModel.find_by_id(id)
        if cadastro_data:
            return cadastro_schema.dump(cadastro_data), 200
        return {'message': NAO_POSSUI_CADASTRO}, 404


class CadastroList(Resource):

    def get(self, ):
        return cadastro_list_schema.dump(CadastroModel.find_all()), 200


    @cadastro_ns.expect(item)
    @cadastro_ns.doc('Create Item')
    def post(self, ):
        cadastro_json = request.get_json()
        cadastro_data = cadastro_schema.load(cadastro_json)

        cadastro_data.save_to_db()

        return cadastro_schema.dump(cadastro_data), 201