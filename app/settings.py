import os
from dotenv import load_dotenv


load_dotenv(".env")

SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')
