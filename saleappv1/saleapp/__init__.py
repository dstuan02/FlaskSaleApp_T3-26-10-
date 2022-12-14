from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/it01saledbv1?charset=utf8mb4' \
                                        % quote('Admin@123') # quote('password')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db means 'database'
db = SQLAlchemy(app=app)