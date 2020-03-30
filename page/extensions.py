from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from google.cloud import firestore

db = firestore.Client()
cors = CORS()
migrate = Migrate()
jwt = JWTManager()
api = Api()
