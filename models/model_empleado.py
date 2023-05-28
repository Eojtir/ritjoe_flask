from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import types
from db import conexion



class EmpleadoModel(conexion.Model):

    id = Column(type_= types.Integer,autoincrement=True,primary_key=True)
    nombre = Column(type_=types.VARCHAR(200),nullable=False)
    apellido = Column(type_=types.VARCHAR(200),nullable=True)
    email = Column(type_=types.VARCHAR(200),nullable=False,unique=True)
    area_id = Column(ForeignKey(column='areas.id'),type_=types.Integer,nullable=False)



    __tablename__ = 'empleados'