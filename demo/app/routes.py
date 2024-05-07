from app import app
from flask import render_template, Flask, request, flash, abort, redirect, url_for, jsonify
from app import database as db_helper

@app.route("/querySong/<userid>/<page>", methods=['POST', 'GET'])
def querySong(page,userid):
    name=""
    if request.method == "POST":
        name = request.values.get('name')
        songs =db_helper.search_songs_by_keyword(name,int(page))
        return render_template("querySong.html", songs=songs, nextpage=str(int(page)+1), prevpage=str(int(page)-1),page=str(page), length=len(songs),name=name, userid=userid)
    else:
        songs = db_helper.fetch_song(int(page))
        return render_template("querySong.html", songs=songs, nextpage=str(int(page)+1), prevpage=str(int(page)-1),page=str(page), length=len(songs), userid=userid)


@app.route('/query1/<userid>/<page>', methods=['POST', 'GET'])
def query1(page,userid):
    genre = request.values.get('genre')
    if genre==None:
        genre=""
    list1 = db_helper.query1(genre,int(page))
    return render_template("query1.html", list1=list1,genre=genre,nextpage=str(int(page)+1), prevpage=str(int(page)-1),page=str(page), length=len(list1), userid=userid)


@app.route('/query2/<userid>/<page>', methods=['POST', 'GET'])
def query2(page,userid):
    list2 = db_helper.query2(int(page))
    return render_template("query2.html", list2=list2,nextpage=str(int(page)+1), prevpage=str(int(page)-1),page=str(page), length=len(list2), userid=userid)

@app.route('/', methods=['POST', 'GET'])
def login():
    username=""
    password=""
    result=False
    
    if request.method == "POST":
        username= request.values.get('username')
        password=request.values.get('password')
        userid= db_helper.checkaccount(username, password)
        if userid!=None:
            url=url_for('homepage',userid=userid)
            return redirect(url)
        result=True
    
    return render_template("log_in.html",result=result)

@app.route('/createaccount', methods=['POST', 'GET'])
def createaccount():
    if request.method == "POST":
        username= request.values.get('username')
        password=request.values.get('password')
        name=request.values.get('name')
        db_helper.createaccnt(username,password,name)
        url=url_for('login')
        return redirect(url)
    return render_template("crtacnt.html")



# Prerna's Code Below:
@app.route("/delete/<song_id>/<user_id>", methods=['POST'])
def delete(song_id,user_id):
    print("in delete")
    print(user)
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(song_id,user_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<song_id>/<user_id>", methods=['POST'])
def update(song_id, user_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        db_helper.update_task_entry(song_id, data["description"],user_id)
        result = {'success': True, 'response': 'Task Updated'}

    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create/<user_id>", methods=['POST'])
def create(user_id):
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_new_task(data['description'],user_id)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route('/user/find_song/<name>')
def find_song(name):
    items = db_helper.fetch_genre(name)
    return render_template("genre.html", items=items)

@app.route('/home/<userid>')
def homepage(userid):
    return render_template("homepage.html",userid=userid)

@app.route('/user/<userid>')
def user(userid):
    items,name, recs = db_helper.fetch_todo(userid)
    return render_template("index.html", items=items, name=name,userid=userid,recs=recs)







