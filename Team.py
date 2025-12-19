from Club import Club
from exceptions import InvalidScoreError


class Team(Club):
    def __init__(self, name: str, city: str, played: int = 0, points: int = 0,
                 goals_scored: int = 0, goals_conceded: int = 0):
        super().__init__(name, city)
        self._played = played
        self._points = points
        self._goals_scored = goals_scored
        self._goals_conceded = goals_conceded

    @property
    def played(self):
        return self._played

    @property
    def points(self):
        return self._points

    @property
    def goals_scored(self):
        return self._goals_scored

    @goals_scored.setter
    def goals_scored(self, value):
        raise AttributeError("Нельзя напрямую изменять goals_scored. Используйте register_match.")

    @property
    def goals_conceded(self):
        return self._goals_conceded

    @goals_conceded.setter
    def goals_conceded(self, value):
        raise AttributeError("Нельзя напрямую изменять goals_conceded. Используйте register_match.")

    def register_match(self, scored: int, conceded: int):
        if not isinstance(scored, int) or not isinstance(conceded, int):
            raise InvalidScoreError("Количество голов должно быть целым числом.")
        if scored < 0 or conceded < 0:
            raise InvalidScoreError("Количество голов не может быть отрицательным.")

        self._played += 1
        self._goals_scored += scored
        self._goals_conceded += conceded

        if scored > conceded:
            self._points += 3
        elif scored == conceded:
            self._points += 1

    def __str__(self):
        return (f"{self.name} ({self.city}): "
                f"Игры: {self.played}, Очки: {self.points}, "
                f"Забито: {self.goals_scored}, Пропущено: {self.goals_conceded}")

    def __repr__(self):
        return self.__str__()
