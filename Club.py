from abc import ABC, abstractmethod

class Club(ABC):
    def __init__(self, name: str, city: str):
        if not name or not isinstance(name, str):
            raise ValueError("Имя клуба должно быть непустой строкой.")
        if not city or not isinstance(city, str):
            raise ValueError("Город должен быть непустой строкой.")

        self._name = name
        self._city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Имя клуба должно быть непустой строкой.")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Город должен быть непустой строкой.")
        self._city = value

    @abstractmethod
    def register_match(self, scored: int, conceded: int):
        pass
