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


def late_list(grades: dict[str, str], deadline_date: str) -> list[str]:
    """Определяет, сколько студентов из определённого списка
    сдали работу позже намеченного срока, и возвращает список фамилий этих
    студентов в алфавитном порядке."""
    late_students = []
    for student, date in grades.items():
        try:
            if deadline_score(date, deadline_date) < 5:
                late_students.append(student)
        except ValueError as e:
            print(f"Пропущен {student}: {e}")
    late_students.sort()
    return late_students


def get_surname():

    while True:
        surname = input("Введите фамилию. В фамилии могут быть только буквы: ").strip()
        if not surname.isalpha():
            print("Ошибка! В фамилии могут быть только буквы!")
            continue
        return surname


def get_date(note: str):
    while True:
        date = input(f"{note} (DD.MM.YYYY): ")
        try:
            parse_date(date)
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue
        return date


def print_menu():
    print("\n--------- МЕНЮ ----------")
    print("1. Оценка студента с учетом дедлайна")
    print("2. Вывести список студентов, пропустивших дедлайн")
    print("0. Выход")
    print("---------------------------")
