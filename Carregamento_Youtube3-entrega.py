from googleapiclient.discovery import build
import pymongo
from pymongo.server_api import ServerApi

# Criação do banco de dados no mongoDB
client = pymongo.MongoClient("mongodb+srv://insira-seu-usuario:insira-a-senha@cluster0.tjdbym4.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
db_youtube1 = db.db_youtube1

# Conexão com a API
youTubeApiKey = 'insira-aqui-sua-chave-de-API'
youtube1 = build('youtube','v3', developerKey=youTubeApiKey)

# Parâmetros da playlist do  youtube o qual será baixado as informações
playlistId = 'PLel8GFCBzYZieMr62IESNyRYstOGu-qDY' # My Hendrix covers
# playlistId = 'PLel8GFCBzYZgoFt7nTYQUOe4m9fGA4bX1' # Miscellaneous covers
playlistName = 'Play As The Original'
nextPage_token = None

# Busca de todos os videos dentro da playlist
playlist_videos = []
while True:
  res = youtube1.playlistItems().list(part='snippet', playlistId = playlistId, maxResults=50, pageToken=nextPage_token).execute()
  insercao = db_youtube1.insert_one(res).inserted_id
  playlist_videos += res['items']
  nextPage_token = res.get('nextPageToken')
  if nextPage_token is None:
    break
print("Número total de vídeos na Playlist: ", len(playlist_videos))


# Criação do banco de dados no mongoDB
client = pymongo.MongoClient("mongodb+srv://insira-seu-usuario:insira-a-senha@cluster0.tjdbym4.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
db_youtube2 = db.db_youtube2

stats = []
for i in range(len(playlist_videos)):
  video_id = playlist_videos[i]['snippet']['resourceId']['videoId']
  res2 = youtube1.videos().list(part='statistics', id=video_id).execute()
  insercao = db_youtube2.insert_one(res2).inserted_id
  stats += res2['items']

print(f'\nCARREGAMENTO DO BANCO DE DADOS REALIZADO COM SUCESSO\n')