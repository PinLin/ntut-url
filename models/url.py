from datetime import datetime

from extensions.db import db


class Url(db.Model):
    name = db.Column(db.String, primary_key=True)
    target = db.Column(db.String, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    @staticmethod
    def create(name: str, target: str):
        """建立縮網址"""
        url = Url(name=name, target=target)

        db.session.add(url)
        db.session.commit()

        return url

    @staticmethod
    def find(name: str):
        """取得縮網址"""
        return Url.query.filter_by(name=name).first()
