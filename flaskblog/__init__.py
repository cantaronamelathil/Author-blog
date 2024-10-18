import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY']= 'dce0c83f11ed92d69468d41c82862fb1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME']= os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')
app.config['MAIL_USERNAME'] = 'cantaronamelathil@gmail.com'  
app.config['MAIL_PASSWORD'] = 'gicq kfss rvbr gdtu'

mail = Mail(app)
from flaskblog import routes
