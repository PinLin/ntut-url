from models.url import Url


class RedirectService:
    @staticmethod
    def is_exist(name: str):
        """
        檢查短網址是否存在
        """
        return Url.find(name) != None

    @staticmethod
    def get_target(name: str):
        """
        取得短網址目標
        """
        return Url.find(name).target
