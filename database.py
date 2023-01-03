import mysql.connector
import env

db = mysql.connector.connect(**env.config)
cursor = db.cursor()