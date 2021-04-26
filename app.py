# from os import environ
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# # Get environment variables on server
# USERNAME = environ.get('RDS_USERNAME')
# PASSWORD = environ.get('RDS_PASSWORD')
# HOSTNAME = environ.get('RDS_HOSTNAME')
# PORT = environ.get('RDS_PORT')
# DBNAME = environ.get('RDS_DB_NAME')

# Syntax: dialect+driver://username:password@host:port/database
# application.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'

# In tests. Creates a file dataowner_sqlite.db in same dir as this file.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataowner_sqlite.db'

# To avoid warning. We do not use the Flask-SQLAlchemy event system, anyway.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class DataOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Since "id" is builtin
    name = db.Column(db.String(64), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=True)
    email = db.Column(db.String(256), unique=False, nullable=False)

    def __repr__(self):
        return f"<Data set {self.id}>"


db.create_all()


@app.route('/', methods=['GET'])
def index():
    owners = DataOwner.query.order_by(DataOwner.id).all()
    return render_template('index.html', owners=owners)


@app.route('/', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    new_owner = DataOwner(name=name, age=age, email=email)
    try:
        db.session.add(new_owner)
        db.session.commit()
        return redirect('/')
    except Exception:
        return "There was an error adding your data owner."


@app.route('/update/<int:id>', methods=['GET'])
def update_get(id):
    owner = DataOwner.query.get_or_404(id)
    return render_template('update.html', owner=owner)


@app.route('/update/<int:id>', methods=['POST'])
def update_post(id):
    # return "Here"
    owner = DataOwner.query.get_or_404(id)
    owner.name = request.form['name']  # Keys are "name"s of input fields (not "id"s)
    owner.age = request.form['age']
    owner.email = request.form['email']
    try:
        db.session.commit()
        return redirect('/')
    except Exception:
        return "There was an error updating your task."


@app.route('/delete/<int:id>')
def delete(id):
    owner_to_delete = DataOwner.query.get_or_404(id)
    try:
        db.session.delete(owner_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception:
        return "There was a problem deleting that owner."


# Not needed if we start with "flask run" (or "python -m flask run")
# if __name__ == '__main__':
#     application.debug = True

#     # Start Flask app
#     application.run()
