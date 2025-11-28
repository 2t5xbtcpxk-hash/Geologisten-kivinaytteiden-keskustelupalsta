from flask import Flask
from flask import redirect, render_template, request, session, abort, flash
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import secrets
import config
import sqlite3
import db, users, forum
import markupsafe

# Connect to database
con = sqlite3.connect("database.db")

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    #check_csrf()
    if "user_id" not in session:
        return render_template("main.html", threads = forum.get_threads())
    else:    
        user_id = session["user_id"]
        return render_template("main.html", threads = forum.get_threads(), user = forum.get_user(user_id))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            flash("VIRHE: väärä tunnus tai salasana")
            return redirect("/login")

@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect("/")

@app.route("/register")
def register():
    if "filled" not in session:
        filled = ""
    else:
        filled = session["filled"]
    return render_template("register.html", filled=filled)

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("VIRHE: Salasanat eivät täsmää.")
        session["filled"] = {"username": username}
        return redirect("/register")
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        flash("VIRHE: Käyttäjänimi on jo varattu.")
        session["filled"] = {"username": username}
        return redirect("/register")

    session.pop("filled", default=None)
    flash("Tunnuksen luominen onnistui, kirjaudu nyt sisään.")
    return redirect("/login")

@app.route("/new_thread", methods=["POST"])
def new_thread():

    require_login()
    check_csrf()

    title = request.form["title"]
    comment = request.form["comment"]
    user_id = session["user_id"]
    rock_type = request.form["rock_type"]
    rock = request.form["rock"]
    latitude = request.form["latitude"]
    longitude = request.form["longitude"]
    collectiondate = request.form["collectiondate"]

    if not comment or len(comment) > 1000:
        abort(403)

    if not title or len(title) > 100:
        abort(403)

    if not rock or len(rock) > 100:
        abort(403)

    if not latitude or len(latitude) > 50:
        abort(403)

    if not longitude or len(longitude) > 50:
        abort(403)

    if not rock_type:
        abort(403)

    thread_id = forum.add_thread(title, comment, user_id, rock_type, rock, latitude, longitude, collectiondate)
    return redirect("/thread/" + str(thread_id))

@app.route("/thread/<int:thread_id>")
def show_thread(thread_id):
    thread = forum.get_thread(thread_id)

    if not thread:
        abort(404)

    messages = forum.get_messages(thread_id)
    return render_template("thread.html", thread=thread, messages=messages)

@app.route("/new_message", methods=["POST"])
def new_message():

    require_login()
    check_csrf()

    content = request.form["content"]
    user_id = session["user_id"]
    thread_id = request.form["thread_id"]

    if not content or len(content) > 1000:
        abort(403)

    try:
        forum.add_message(content, user_id, thread_id)
    except:
        abort(403)

    return redirect("/thread/" + str(thread_id))

@app.route("/edit/<int:message_id>", methods=["GET", "POST"])
def edit_message(message_id):

    require_login()

    message = forum.get_message(message_id)

    if not message:
        abort(404)

    check_user(message["user_id"])

    if request.method == "GET":
        return render_template("edit.html", message=message)

    if request.method == "POST":
        content = request.form["content"]
        check_csrf()

        if not content or len(content) > 1000:
            abort(403)

        forum.update_message(message["id"], content)
        return redirect("/thread/" + str(message["thread_id"]))
    
@app.route("/remove/<int:message_id>", methods=["GET", "POST"])
def remove_message(message_id):

    require_login()

    message = forum.get_message(message_id)
    
    if not message:
        abort(404)
    
    check_user(message["user_id"])

    if request.method == "GET":
        return render_template("remove.html", message=message)

    if request.method == "POST":
        check_csrf()
        if "continue" in request.form:
            forum.remove_message(message["id"])
        return redirect("/thread/" + str(message["thread_id"]))
    
@app.route("/remove_thread/<int:thread_id>", methods=["GET", "POST"])
def remove_thread(thread_id):

    require_login()

    thread = forum.get_thread(thread_id)

    if not thread:
        abort(404)

    check_user(thread["user_id"])

    if request.method == "GET":
        return render_template("remove_thread.html", thread=thread)

    if request.method == "POST":
        check_csrf()
        if "continue" in request.form:
            forum.remove_thread(thread["id"])
        return redirect("/")
    
@app.route("/edit_thread/<int:thread_id>", methods=["GET", "POST"])
def edit_thread(thread_id):

    require_login()

    thread = forum.get_thread(thread_id)

    if not thread:
        abort(404)

    check_user(thread["user_id"])

    if request.method == "GET":
        return render_template("edit_thread.html", thread=thread)

    if request.method == "POST":
        title = request.form["title"]
        comment = request.form["comment"]
        rock_type = request.form["rock_type"]
        rock = request.form["rock"]
        latitude = request.form["latitude"]
        longitude = request.form["longitude"]
        collectiondate = request.form["collectiondate"]
        check_csrf()

        if not comment or len(comment) > 1000:
            abort(403)

        if not title or len(title) > 100:
            abort(403)

        if not rock or len(rock) > 100:
            abort(403)

        if not latitude or len(latitude) > 50:
            abort(403)

        if not longitude or len(longitude) > 50:
            abort(403)

        if not rock_type:
            abort(403)

        forum.update_thread(thread["id"], title, comment, rock, rock_type, latitude, longitude, collectiondate)
        return redirect("/")
    
@app.route("/search")
def search():
    query = request.args.get("query")
    results = forum.search(query) if query else []
    return render_template("search.html", query=query, results=results)

@app.route("/user/<int:user_id>")
def show_user(user_id):

    require_login()

    user = users.get_user(user_id)

    if not user:
        abort(404)

    if user["user_id"] != session["user_id"]:
        abort(403)

    threads = users.get_threads(user_id)
    return render_template("user.html", user=user, threads=threads)
    
@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():

    print(session["csrf_token"])
    print(request.form["csrf_token"])
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

def check_user(user):

    if user != session["user_id"]:
        abort(403)