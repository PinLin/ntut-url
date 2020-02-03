from extensions.db import db
from models.url import Url


class RedirectService:
    @staticmethod
    def get_target(name: str):
        """
        取得縮網址目標
        """
        return Url.find(name).target

    @staticmethod
    def click_url(name: str):
        """
        點擊縮網址
        """
        url = Url.find(name)
        url.clicks += 1
        db.session.add(url)
        db.session.commit()
