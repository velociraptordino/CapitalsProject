"""
File: model.py
Editor: Tiffany Nguyen
Date: December 5, 2019
Section: 01
Email: tn4@umbc.edu
Description: The player class is used to write the data scraped from the
website into a database
Program Assumptions:
- only players' numbers and names are unique
- flask alchemy is being used
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, unique=True, nullable=False)
    lastName = db.Column(db.String, unique=True, nullable=False)
    special = db.Column(db.String, unique=False, nullable=True)
    number = db.Column(db.Integer,unique=True, nullable=False)
    position = db.Column(db.String, unique=False, nullable=False)
    shoots = db.Column(db.String, unique=False, nullable=False)
    height = db.Column(db.String,unique=False, nullable=False)
    weight = db.Column(db.Integer,unique=False, nullable=False)
