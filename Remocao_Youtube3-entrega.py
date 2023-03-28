import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://insira-seu-usuario:insira-a-senha@cluster0.tjdbym4.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test

nome_db = 'db_youtube1'
db[nome_db].drop()

print(f'\nREMOÇAO DO BANCO DE DADOS "{nome_db}" REALIZADO COM SUCESSO\n')


nome_db = 'db_youtube2'
db[nome_db].drop()

print(f'\nREMOÇAO DO BANCO DE DADOS "{nome_db}" REALIZADO COM SUCESSO\n')