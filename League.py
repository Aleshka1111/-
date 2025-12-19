import json
from Team import Team
from exceptions import TeamNotFoundError, TeamHomeAwayError, InvalidScoreError


class League:
    def __init__(self, league_name: str):
        self.name = league_name
        self._teams: list[Team] = []

    def add_team(self, team: Team):
        if any(t.name == team.name for t in self._teams):
            raise ValueError(f"Команда с именем '{team.name}' уже существует в лиге.")
        self._teams.append(team)

    def remove_team(self, name: str):
        for team in self._teams:
            if team.name == name:
                self._teams.remove(team)
                return
        raise ValueError(f"Команда с именем '{name}' не найдена.")

    def __getitem__(self, index_or_name):
        if isinstance(index_or_name, int):
            if 0 <= index_or_name < len(self._teams):
                return self._teams[index_or_name]
            else:
                raise IndexError("Индекс вне диапазона.")
        elif isinstance(index_or_name, str):
            for team in self._teams:
                if team.name == index_or_name:
                    return team
            raise TeamNotFoundError(f"Команда '{index_or_name}' не найдена.")
        else:
            raise TypeError("Индекс должен быть int или str.")

    def __iter__(self):
        return iter(self._teams)

    def get_standings(self):
        """Возвращает отсортированный список команд по спортивному принципу."""
        return sorted(
            self._teams,
            key=lambda t: (-t.points, -(t.goals_scored - t.goals_conceded), t.name)
        )

    def play_match(self, home_name: str, away_name: str, home_goals: int, away_goals: int):
        if not isinstance(home_goals, int) or not isinstance(away_goals, int):
            raise InvalidScoreError("Счёт должен быть целым числом.")
        if home_goals < 0 or away_goals < 0:
            raise InvalidScoreError("Счёт не может быть отрицательным.")

        if home_name == away_name:
            raise TeamHomeAwayError("Хозяин и гость не могут быть одной командой.")

        home_team = self[home_name]
        away_team = self[away_name]
        home_team.register_match(home_goals, away_goals)
        away_team.register_match(away_goals, home_goals)

    @classmethod
    def from_json(cls, path: str) -> 'League':
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        league = cls(data["league_name"])

        for team_data in data["teams"]:
            team = Team(
                name=team_data["name"],
                city=team_data["city"],
                played=team_data["played"],
                points=team_data["points"],
                goals_scored=team_data["goals_scored"],
                goals_conceded=team_data["goals_conceded"]
            )
            league.add_team(team)

        return league

    def to_json(self, path: str):
        data = {
            "league_name": self.name,
            "teams": [
                {
                    "name": team.name,
                    "city": team.city,
                    "played": team.played,
                    "goals_scored": team.goals_scored,
                    "goals_conceded": team.goals_conceded,
                    "points": team.points
                }
                for team in self._teams
            ]
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
