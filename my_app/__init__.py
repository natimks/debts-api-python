from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MySql2020!@localhost/workshop-python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from my_app.person import endpoints as person_endpoints
from my_app.debt import endpoints as debt_endpoints

app.register_blueprint(person_endpoints.person_route)
app.register_blueprint(debt_endpoints.debt_route)

db.create_all()
