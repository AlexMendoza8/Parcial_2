from flask import Flask, render_template
import requests,os
from flask_sqlalchemy import SQLAlchemy
from website import create_app

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app()

# Build the Sqlite ULR for SqlAlchemy
sqlite_url = "sqlite:///" + os.path.join(basedir, "parcial_2.db")

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)
db.init_app(app)


if __name__ == '__main__':
  app.run(debug=True)
