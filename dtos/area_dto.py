from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.model_area import AreaModel


class AreasRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel

class AreasResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel