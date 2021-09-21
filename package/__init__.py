<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'
app.config['SECRET_KEY'] = '2392510167989ae56f41070a'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login_page'
#login_manager.login_message_category = 'info'
from package import routes

=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'
app.config['SECRET_KEY'] = '2392510167989ae56f41070a'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login_page'
#login_manager.login_message_category = 'info'
from package import routes

>>>>>>> ed308709c676f4184795b560223312a0dc576934
