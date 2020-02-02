from extensions.db import db
from models.url import Url
from utils.generate_name import generate_name


class UrlsService:
    @staticmethod
    def is_exist(name: str):
        """
        檢查縮網址是否存在
        """
        return Url.find(name) != None

    @staticmethod
    def create_new_url(name: str, target: str):
        """
        新增縮網址
        """
        # 如果沒有指定 name 就隨機產生一個
        while not name or UrlsService.is_exist(name):
            name = generate_name(6)

        # target 沒有指明協定就在開頭加上 http://
        if not '://' in target:
            target = 'http://' + target

        # 建立縮網址
        url = Url(name=name, target=target)

        db.session.add(url)
        db.session.commit()

        return {
            'name': url.name,
            'target': url.target,
        }
