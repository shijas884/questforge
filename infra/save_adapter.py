# python
from abc import ABC,abstractmethod
import json


class SaveAdapter(ABC):

    @abstractmethod
    def save(self, data:dict) -> None:
        pass

    @abstractmethod 
    def load(self) -> dict:
        pass


class JsonFileAdapter(SaveAdapter):

    def __init__(self, path:str = 'save.json'):
        self.path = path

    def save(self, data) -> None:
        with open(self.path) as f:
            json.dump(data, f, indent=2)

    def load(self):
        with open(self.path) as f:
            return json.load(f)


class InMemoryAdapter(SaveAdapter):

    def __init__(self):
       self._data: dict = {}

    def save(self, data) -> None:
        self._data = data

    def load(self) -> dict:
        return self._data

    

         