import json
from dataclasses import dataclass

@dataclass
class PasswordEntry:
    title: str
    username: str
    password: str
    notes: str
        
    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(**data)
