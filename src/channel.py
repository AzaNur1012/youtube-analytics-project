import json
import os
from googleapiclient.discovery import build

#class YoutubeParser:
    #api_key = os.getenv('YT_API_KEY')
    #youtube = build('youtube', 'v3', developerKey=api_key)

    #@classmethod
    #def get_channel(cls,channel_id):
        #yt_channel_all_info = cls.youtube.channels().list(id=channel_id, part='snippet,statistics').execute
        #return yt_channel_all_info

class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube: object = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        #self.info = YoutubeParser.get_channel(channel_id)

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_id))
