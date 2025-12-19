class TeamNotFoundError(Exception):
    """Команда с указанным именем не найдена"""
    pass


class TeamHomeAwayError(Exception):
    """Хозяин и гость — одна и та же команда"""
    pass


class InvalidScoreError(Exception):
    """Некорректный счёт (не число или отрицательное значение)"""
    pass