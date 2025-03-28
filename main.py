# Laboratorio 7 - Base de Datos
# Fabiola Contreras
# Diego Duarte
# Maria Jose Villafuerte

from sqlalchemy import create_engine
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Leer la URI desde las variables de entorno
MONGO_URI = os.getenv("MONGO_URI")

# Conectar a MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["Laboratorio7"]

# Verificar conexión
print(db.list_collection_names())  # Ver las colecciones disponibles

