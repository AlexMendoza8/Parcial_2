from .db import db, BaseModelMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


class sarampion_panama(db.Model, BaseModelMixin):
    __tablename__ = 'sarampion_panama'
    year = db.Column(db.Integer , primary_key=True)
    porcentage = db.Column(db.Integer,nullable=True)
    country = db.Column(db.String ,nullable=True)
    code = db.Column(db.String ,nullable=True)

    

    


