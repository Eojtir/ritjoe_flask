from flask_restful import Resource, request
from db import conexion
from models.model_area import AreaModel
from dtos.area_dto import AreasRequestDto, AreasResponseDto


class AreaController(Resource):
    def post(self):
        data = request.json
        try:
            dto = AreasRequestDto()
            dataValidada = dto.load(data)
            nuevaArea = AreaModel(**dataValidada)
            conexion.session.add(nuevaArea)
            conexion.session.commit()

            return {
                'message': 'Area creada exitozamente'
            }

        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'error al crear el Area',
                'content': error.args
            }, 201

    def get(self, id):

        try:
            resultado = conexion.session.query(AreaModel).filter_by(id=id).first()
            dto = AreasResponseDto()
            data = dto.dump(resultado)
            status = 200
            if len(data)==0:
                data = 'no existe ningun area con ese id'
                status = 400

            return {
                'content': data
            },status
        except Exception as error:
            return {
                'message': 'Error',
                'content': error.args
            }

