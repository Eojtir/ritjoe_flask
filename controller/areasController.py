from flask_restful import Resource,request
from db import conexion
from models.model_area import AreaModel
from dtos.area_dto import AreasRequestDto,AreasResponseDto

class AreasController(Resource):
    def get(self):
            resultado = conexion.session.query(AreaModel).all()
            dto = AreasRequestDto(many = True)
            data = dto.dump(resultado)
            
            return {
            'content': data
        }