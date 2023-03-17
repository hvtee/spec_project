import uuid
import datetime


class Note:
    def __init__(self, id=str(uuid.uuid1())[0:4],
                 title="text",
                 body="text",
                 date=str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self._id = id
        self._title = title
        self._body = body
        self._date = date

    def __del__(self):
        return None

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_body(self):
        return self._body

    def get_date(self):
        return self._date

    def set_id(self):
        self._id = str(uuid.uuid1())[0:4]

    def set_date(self):
        self._date = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def set_title(self, tile: str):
        self._title = tile

    def set_body(self, body: str):
        self._body = body

    def to_string(self):
        return self._id + ';' + self._date + ';' + self._title + ';' + self._body
