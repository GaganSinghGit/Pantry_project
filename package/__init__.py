from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
import pymysql
import os
#pymysql.install_as_MySQLdb()
#from flask_login import LoginManager



app = Flask(__name__)
app.config['MYSQL_USER'] = 'uh1lpxveaoe75wvj'
app.config['MYSQL_PASSWORD'] = 'TTUpXWH7KdfBQHBmfIZZ'
app.config['MYSQL_HOST'] = 'bgpteeqexi1aiwxd0d4c-mysql.services.clever-cloud.com'
app.config['MYSQL_DB'] = 'bgpteeqexi1aiwxd0d4c'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config['SECRET_KEY'] = '2392510167989ae56f41070a'
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
#db = SQLAlchemy(app)
mysql = MySQL(app)
bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login_page'
#login_manager.login_message_category = 'info'
from package import routes

