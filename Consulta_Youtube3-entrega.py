from pymongo.server_api import ServerApi
import pymongo
import pandas as pd


client = pymongo.MongoClient("mongodb+srv://insira-seu-usuario:insira-a-senha@cluster0.tjdbym4.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
db_youtube1 = db.db_youtube1


videos_ids = []
videos_title = []
published_dates = []
videos_description = []
url_thumbnails = []

for item in db_youtube1.find():
  for i in range(len(item['items'])):
    videos_id = item['items'][i]['snippet']['resourceId']['videoId']
    video_title = item['items'][i]['snippet']['title']
    published_date = item['items'][i]['snippet']['publishedAt']
    video_description = item['items'][i]['snippet']['description']
    url_thumbnail = item['items'][i]['snippet']['thumbnails']['high']['url']
    videos_ids.append(videos_id)
    videos_title.append(video_title)
    published_dates.append(published_date)
    videos_description.append(video_description)
    url_thumbnails.append(url_thumbnail)


client = pymongo.MongoClient("mongodb+srv://insira-seu-usuario:insira-a-senha@cluster0.tjdbym4.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
db_youtube2 = db.db_youtube2

likes = []
views = []
comments = []
for item in db_youtube2.find():
  liked = item['items'][0]['statistics']['likeCount']
  view = item['items'][0]['statistics']['viewCount']
  comment = item['items'][0]['statistics']['commentCount']

  likes.append(liked)
  views.append(view)
  comments.append(comment)


# Criação do dataframe com base nos dados coletados da API
playlist_df = pd.DataFrame({
      'title':videos_title,
      'video_id':videos_ids,
      'video_description':videos_description,
      'published_date':published_dates,
      'likes':likes,
      'views':views,
      'comment':comments,
      'thumbnail': url_thumbnails
      })


# converter colunas de strings em inteiro
playlist_df['likes'] = playlist_df['likes'].astype(int)
playlist_df['views'] = playlist_df['views'].astype(int)

# # Adição de uma coluna do valor percentual de likes em relaçao a views
playlist_df['likes/views'] = playlist_df['likes'] / playlist_df['views'] *100

# # Exibiçao do dataframe, ordenado pela razão likes/views
print('\nResults based on likes/views: \n',playlist_df.sort_values(by='likes/views', ascending=False)[['title','likes/views','likes','views','comment','thumbnail']]) # Exibição de todas as linhas do dataframe
# print('\nResults of 10 first lines based on likes/views: \n',playlist_df.sort_values(by='likes/views', ascending=False)[['title','likes/views','likes','views','comment','thumbnail']].head(10)) # Filtro opcional