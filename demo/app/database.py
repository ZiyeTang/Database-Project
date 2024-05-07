import random
import pymysql
from app import db
def fetch_song(start:int) -> dict:
    results=[]
    start=(start-1)*20
    conn = db.connect()
    sqlStr="SELECT song_name, artist_name, album_name, song_popularity, song_type, song_id from song,artist, album where substring(song.artist_id,1,(select length(song.artist_id)-1))=artist.artist_id and song.album_id=album.album_id order by song_name limit "+str(start)+", 20;"
    results = conn.execute(sqlStr).fetchall()
    conn.close()
    
    song_list=[]
    for r in results:
        item={
            "song_name": r[0],
            "artist_name": r[1],
            "album_name": r[2],
            "song_popularity": r[3],
            "song_type": r[4],
            "song_id":r[5]
        }
        song_list.append(item)
    
    return song_list

def search_songs_by_keyword(name,start:int):
    start=(start-1)*20
    conn = db.connect()

    sqlStr="SELECT song_name, artist_name, album_name, song_popularity, song_type,song_id from song,artist, album  where substring(song.artist_id,1,(select length(song.artist_id)-1))=artist.artist_id and song.album_id=album.album_id and (song_name like %s or artist_name like %s or album_name like %s) order by song_name limit "+str(start)+", 20;"
    args=['%'+name+'%','%'+name+'%','%'+name+'%']
    results = conn.execute(sqlStr,args).fetchall()
    conn.close()
    song_list = []
    for r in results:
        item = {
            "song_name": r[0],
            "artist_name": r[1],
            "album_name": r[2],
            "song_popularity": r[3],
            "song_type": r[4],
            "song_id": r[5]
        }
        song_list.append(item)
    return song_list

def query1(genre,start:int):
    start=(start-1)*20
    sqlStr= ("SELECT al.album_name,al.album_popularity,art.artist_name,art.popularity, art.genre "
            "FROM  album al,(SELECT	a.artist_id,	a.artist_name,a.genre,	temp.popularity"
           " FROM artist a NATURAL JOIN (SELECT  Max(artist_popularity) AS popularity, genre	"
           "FROM	artist ar 	GROUP BY genre) AS temp WHERE 	temp.popularity = a.artist_popularity	"
            "AND a.genre = temp.genre 	) AS art "
           " WHERE	al.artist_id = art.artist_id AND al.album_popularity IS NOT NULL"
           " AND al.album_popularity > 50  AND art.popularity > 50 AND art.genre like %s ORDER BY art.artist_name,al.album_name limit ")+str(start)+", 20;"
    args=['%'+genre+'%']
    conn = db.connect()
    results = conn.execute(sqlStr,args).fetchall()
    conn.close()
    static_list1 = []
    for r in results:
        item = {
            "album_name": r[0],
            "album_popularity": r[1],
            "artist_name": r[2],
            "artist_popularity": r[3],
            "artist_genre":r[4]
        }
        static_list1.append(item)
    return  static_list1


def query2(start:int):
    start=(start-1)*20
    sqlStr= ("select s.song_name,s.song_popularity,a.album_name,a.album_popularity "
        "from song s join album a on s.album_id=a.album_id where(select count(song_id) "
         "from song s1 where s1.album_id=a.album_id group by s1.album_id)>5 "
         "order by a.album_id limit ")+str(start)+", 20;"
    conn = db.connect()
    results = conn.execute(sqlStr).fetchall()
    conn.close()
    static_list2 = []
    for r in results:
        item = {
            "song_name": r[0],
            "song_popularity": r[1],
            "album_name": r[2],
            "album_popularity": r[3]
        }
        static_list2.append(item)
    return  static_list2


def checkaccount(username, password):
    sqlStr="select user_id from user where user_name='"+username+"' and password='"+password+"';"
    conn = db.connect()
    results = conn.execute(sqlStr).fetchall()
    conn.close()
    
    if len(results)==0:
        return None
    return str(results[0][0])


def createaccnt(username, password,name):
    sqlStr1 = "insert into user (user_id) select 100+(select count(user_id) from user);"
    sqlStr2 = "update user set name='"+name+"', user_name='"+username+"', password='"+password+"' where user_id=(select * from (select 99+count(user_id) from user) as temp);"
    conn = db.connect()
    conn.execute(sqlStr1)
    conn.execute(sqlStr2)
    conn.close()

# Prerna's Codes Below:
def fetch_todo(name)->dict:

    conn=db.connect()
    conn.execute("use mymusic;")
    query2='select user_name from user where user_id="{}";'.format(name)
    query='select f.song_id,s.song_name,a.album_name,f.user_id from favorite_song f natural join song s left join album a on s.album_id=a.album_id where user_id={};'.format(name)
    query4='delete from recommendations;'
    query5='CALL mymusic.recommend({});'.format(name)
    query3='select DISTINCT f.song_id,s.song_name,a.album_name,f.user_id from recommendations f natural join song s left join album a on s.album_id=a.album_id where user_id={} LIMIT 8;'.format(name)
    query6='CALL mymusic.CleanTables({});'.format(name)

    results=conn.execute(query)
    infor=conn.execute(query2)
    conn.execute(query4)
    conn.execute(query5)
    conn.execute(query6)
    recResults=conn.execute(query3)
    conn.close()
    songs= []
    users={}
    recs= []
    for res in infor:

        users={"info":res[0]}



    for result in results:
        item = {
            "id":result[0],
            "song":result[1],
            "album":result[2],
            "user":result[3]

        }
        songs.append(item)
    
    for recResult in recResults:
        val = {
            "id":recResult[0],
            "song":recResult[1],
            "album":recResult[2],
            "user":recResult[3]

        }
        recs.append(val)
    return songs, users,recs

def fetch_genre(name:str)->dict:

    conn=db.connect()
    conn.execute("use mymusic;")
    query='select art.genre, al.album_name, art.artist_name, art.popularity from album al, (select a.artist_id, a.artist_name, a.genre, temp.popularity from artist a natural join (select genre, max(artist_popularity) as popularity from artist ar group by genre) as temp where temp.popularity=a.artist_popularity and a.genre=temp.genre) as art where al.artist_id=art.artist_id and art.popularity>50 and al.album_popularity>50 and genre like "%{}%" order by popularity desc, art.artist_name limit 30 ;'.format(name)
    results=conn.execute(query)
    conn.close()
    songs= []

    for result in results:
        item = {
            "gen":result[0],
            "album_name":result[1],
            "art_name":result[2],
            "popu":result[3]
        }
        songs.append(item)
    return songs


def remove_task_by_id(song_id:str,user_id:int)->None:

    conn = db.connect()
    conn.execute("use mymusic;")
    query = 'Delete From favorite_song where song_id = "{}" and user_id={};'.format(song_id, user_id)
    conn.execute(query)
    conn.close()



def update_task_entry(song_id:str, text:str, user_id:int)->None:
    conn = db.connect()
    conn.execute("use mymusic;")
    query = 'Update favorite_song set song_id = "{}" where user_id = {} and song_id="{}";'.format(text,user_id,song_id)
    conn.execute(query)
    conn.close()

def insert_new_task(text:str,user_id:int)->None:
    conn = db.connect()
    conn.execute("use mymusic;")
    
    query = 'Insert Into favorite_song (user_id, song_id) VALUES ({}, "{}");'.format(user_id,
        text)
    query2 = 'CALL mymusic.recommend({})'.format(user_id)
    
    conn.execute(query)
    conn.execute(query2)
    conn.close()
