
import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deva1965",
    database="flight_game"
)
cursor = db.cursor(dictionary=True)


