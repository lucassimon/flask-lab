from apps.db import db


class ForbiddenWords(db.Model):
    __tablename__ = "forbidden_words"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(120), index=True, nullable=False)
    value = db.Column(db.String(120), nullable=False)


class ForbiddenDomains(db.Model):
    __tablename__ = "forbidden_domains"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(120), index=True, nullable=False)
    value = db.Column(db.String(120), nullable=False)
