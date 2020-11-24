import os
from dotenv import load_dotenv
from dotenv.main import find_dotenv
import mysql.connector
load_dotenv(find_dotenv())
print(os.getenv("BOT_TOKEN"))
print(os.getenv('DB_USER'))
print(os.getenv('DB_PASSWORD'))
print(os.getenv('HOST_NAME'))
print(os.getenv('DB_NAME'))
con = mysql.connector.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('HOST_NAME'),
        database=os.getenv('DB_NAME'),
    )