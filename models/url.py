from sqlalchemy.sql import func

from extensions.db import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), unique=True)
    target = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find(name: str):
        """取得縮網址"""
        return Url.query.filter_by(name=name).first()
