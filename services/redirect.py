from models.url import Url


class RedirectService:
    @staticmethod
    def get_target(name: str):
        """
        取得縮網址目標
        """
        return Url.find(name).target
