from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.model_empleado import EmpleadoModel

class EmpleadoRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel
        include_fk = True

class EmpleadoResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel
        include_fk = True
