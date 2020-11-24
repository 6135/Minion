import os
from dotenv import load_dotenv
from dotenv.main import find_dotenv
import mysql.connector
load_dotenv(find_dotenv())
cnx = mysql.connector.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('HOST_NAME'),
        database=os.getenv('DB_NAME'),
    )