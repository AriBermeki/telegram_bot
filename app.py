from cmd import IDENTCHARS
from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from flask_migrate import Migrate
from random import *



app = Flask(__name__)
Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
HTTP_API = os.environ['HTTP_API']


def random_integer():
    min_ = 1000
    max_ = 10000
    rand = randint(min_, max_)
    return rand


class User(db.Model):
    __tablename__= 'telegram_ari'
    id=db.Column( db.Integer, primary_key = True)
    ID = db.Column(db.String(50),  default=random_integer, unique=True)
    email = db.Column(db.String(50))
    



    def __init__(self, ID, email):
        self.ID = ID
        self.email = email
        
       



class Regester(FlaskForm):
    
    email = StringField('Email', validators=[InputRequired(), Length(max=200)])
    ID = StringField(randint(1000, 10000))







migrate = Migrate(app, db)
db.create_all()



@app.route('/regester', methods=['POST', 'GET'])
def regist():
    form = Regester()
    if form.validate_on_submit():

        
        
        user = User(
            ID = form.ID.data,
            email= form.email.data
            )
        db.session.add(user)
        db.session.commit()
        
        
        return '<h1> Succsesful Regestration</h1>'
    return render_template('index.html', form=form)








if __name__=="__main__":
   
    app.run(debug=True)

