from flask import Flask, render_template, redirect, request
import requests
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, login_user, logout_user
from flask.ext.mongoengine.wtf import model_form
from wtforms import PasswordField

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['MONGODB_SETTINGS'] = {'db' : 'users'}
app.config['SECRET_KEY'] = 'open sesame'
app.config['WTF_CSRF_ENABLED'] = True
login_manager = LoginManager()
login_manager.init_app(app)

db = MongoEngine(app)
class User(db.Document):
    name = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    def is_authenticated(self):
        users = User.object(name=self.name, password=self.password)
        return len(users) != 0
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.name

UserForm = model_form(User)
UserForm.password = PasswordField('password')

@login_manager.user_loader
def load_user(name):
    users = User.objects(name=name)
    if len(users) != 0:
        return users[0]
    else:
        return None

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/natalia")
def natalia():
    return render_template("natalia.html")

@app.route("/sammy")
def sammy():
    return render_template("sammy.html")

@app.route("/name/<name_query>")
def name(name_query):
    return name_query

@app.route("/register", methods={"POST", "GET"})
def register():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        form.save()
        return redirect("/")
    return render_template("register.html", form=form)

@app.route('/login', methods={'GET', 'POST'})
def login():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(name=form.name.data, password=form.password.data)
        login_user(user)
        return redirect('/')

    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
