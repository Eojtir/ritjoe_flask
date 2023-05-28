from flask_restful import Resource, request
from db import conexion
from models.model_empleado import EmpleadoModel
from dtos.empleado_dto import EmpleadoRequestDto,EmpleadoResponseDto

class EmpleadoController(Resource):
    def post(self):
        data = request.json
        try:
            dto = EmpleadoRequestDto()
            dataValidada = dto.load(data)
            nuevoempleado = EmpleadoModel(**dataValidada)
            conexion.session.add(nuevoempleado)
            conexion.session.commit()

            return {
                'message': 'Empleado creado exitosamente'
            },201

        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'error al crear el Empleado',
                'content': error.args
            }, 400
