from ma import ma
from models.cadastro import CadastroModel

class CadastroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CadastroModel
        load_instance = True