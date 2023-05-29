from flask import Flask
from db import conexion
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.model_area import AreaModel
from models.model_empleado import EmpleadoModel
from controller.area_controller import AreaController
from controller.areasController import AreasController
from controller.empleado_controller import EmpleadoController
from controller.empleados_controller import EmpleadosController
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api = Api(app=app)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASEURI')
conexion.init_app(app)
Migrate(app, conexion)

api.add_resource(AreaController,'/area','/area/<int:id>')
api.add_resource(AreasController,'/areas')
api.add_resource(EmpleadoController,'/empleado')
api.add_resource(EmpleadosController,'/empleados','/empleados/<string:parametros>')