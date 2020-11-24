import os
from dotenv import load_dotenv
from dotenv.main import find_dotenv
import mysql.connector

def con():
    mysql.connector.connect(user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASSWORD'),
                            host=os.getenv('HOST_NAME'),
                            database=os.getenv('DB_NAME'),
                            )
    