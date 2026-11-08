import datetime
import re


DATE_RE = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")


def parse_date(date_str: str) -> datetime.date:
    """Парсит строку строго в формате DD.MM.YYYY."""
    if not DATE_RE.fullmatch(date_str):
        raise ValueError(
            f"Дата должна быть в формате DD.MM.YYYY, получено: {date_str!r}"
        )
    try:
        return datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError:
        raise ValueError(f"Некорректная дата: {date_str!r}")


def deadline_score(pass_date: str, deadline_date: str) -> int:
    """Определяет, исходя из даты дедлайна и фактической сдачи,
    сколько баллов получит студент за сданную работу"""
    pass_date = parse_date(pass_date)
    deadline_date = parse_date(deadline_date)

    days_late = (pass_date - deadline_date).days

    if days_late <= 0:
        return 5
    elif days_late <= 7:
        return 4
    elif days_late <= 14:
        return 3
    elif days_late <= 21:
        return 2
    elif days_late <= 28:
        return 1
    else:
        return 0
