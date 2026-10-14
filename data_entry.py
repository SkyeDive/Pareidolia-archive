from base64 import b64decode, b64encode
import json
from dataclasses import dataclass

@dataclass
class DataEntry():
    title: str
    filename: str
    data: bytes
    
    def __init__(self, title: str, filename: str, data: str | bytes):
        self.title = title
        self.filename = filename
        if type(data) == str:
            self.data = b64decode(bytes(data,"utf-8"))
        elif type(data) == bytes:
            self.data = data
        else:
            raise Exception("Invalid data type")
    
    def to_json(self) -> str:
        data = dict(self.__dict__)
        data['data'] = b64encode(data['data']).decode('utf-8')
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        data['data'] = b64decode(bytes(data['data'],'utf-8'))
        return cls(**data)
