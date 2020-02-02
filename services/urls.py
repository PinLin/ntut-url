from datetime import datetime, timedelta

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
    def is_expired(name: str):
        """
        檢查短網址是否過期
        """
        url = Url.find(name)

        # 沒有過期時間就代表沒有過期
        if url.expire_time == None:
            return False

        return datetime.now() > url.expire_time

    @staticmethod
    def create_url(name: str, target: str, expire_seconds: int):
        """
        新增縮網址
        """
        # 如果沒有指定 name 就隨機產生一個
        while not name or UrlsService.is_exist(name) and not UrlsService.is_expired(name):
            name = generate_name(6)

        # target 沒有指明協定就在開頭加上 http://
        if not '://' in target:
            target = 'http://' + target

        # 設定過期時間
        if expire_seconds != None:
            expire_time = datetime.now() + timedelta(seconds=expire_seconds)
        else:
            expire_time = None

        # 建立縮網址
        if UrlsService.is_exist(name):
            url = Url.find(name)
            url.target = target
            url.expire_time = expire_time
        else:
            url = Url(name=name, target=target, expire_time=expire_time)

        db.session.add(url)
        db.session.commit()

        return {
            'name': url.name,
            'target': url.target,
        }
