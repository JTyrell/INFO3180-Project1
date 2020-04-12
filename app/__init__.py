from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "MyDiamondDani"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Project1:password@localhost/Project1" #
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

ALLOWED_EXTENSIONS = ['jpg','png','jpeg','gif','tiff','jfif']

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
from app import views
