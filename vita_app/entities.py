days_of_week = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}

times = {
    0: "8:30",
    1: "11:00",
    2: "13:30",
    3: "16:00",
    4: "18:30",
}


class Event():
    def __init__(self, time: str, value: str):
        self.time = time
        self.value = value

    @property
    def is_free(self) -> bool:
        if self.value:
            return False
        return True

    def to_dict(self):
        return {
            "time": self.time,
            "value": self.value,
            "is_free": self.is_free
        }

    def __repr__(self) -> str:
        value = self.value if self.value else "Свободно"
        return f"Окошко - {self.time} - {value} "


class Day:
    def __init__(self, number: int = None, day_of_week: str = None, events: list[Event] = None):
        self.number = number
        self.day_of_week = day_of_week
        self.events = events

    @property
    def is_free(self) -> bool:
        for event in self.events:
            if event.is_free:
                return True
        return False

    def to_dict(self):
        return {
            "number": self.number,
            "day_of_week": self.day_of_week,
            "events": [event.to_dict() for event in self.events],
            "is_free": self.is_free
        }

    def __repr__(self):
        return f"День - {self.number}; День недели - {self.day_of_week}; События - {self.events}"


class Month():

    def __init__(self, days: list[Day], title):
        self.days = days
        self.title = title

    @classmethod
    def from_matrix(cls, matrix: list[list[str]], title: str):
        days = []
        num_of_rows = len(matrix)
        for row in range(0, num_of_rows, 6):
            for col in range(0, 7):
                if matrix[row][col] == '':
                    continue
                day = Day(
                    number=matrix[row][col],
                    day_of_week=days_of_week[col],
                    events=[
                        Event(
                            time=times.get(x),
                            value=matrix[row + 1 + x][col]
                        ) for x in times
                    ],
                )
                days.append(day)
        return cls(days, title)

    def to_dict(self):
        return {
            'title': self.title,
            'days': [day.to_dict() for day in self.days]
        }

    def __repr__(self) -> str:
        return self.title + '\n' + '\n'.join([f"{self.days[x]}" for x in range(0, len(self.days))])
