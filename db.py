from flask import Flask
from mongoengine import connect

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mydatabase',
    'host': 'localhost',
    'port': 27017
}

connect(**app.config['MONGODB_SETTINGS'], alias='octa_db')
