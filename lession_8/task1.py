class Date:

    DEFAULT_YEAR = 2000

    date_string = ""
    year = 0
    month = 0
    day = 0

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def parce(cls, date):
        result = date.date_string.split("-")
        date.year = int(result[2])
        date.month = int(result[1])
        date.day = int(result[0])

        if(date.year < cls.DEFAULT_YEAR):
            date.year = cls.DEFAULT_YEAR

    @staticmethod
    def validate(date):
        if date.month < 0 or date.month > 12:
            raise Exception("Месяц не в диапазоне 1-12")


def task_1():
    date = Date("12-11-1990")
    Date.parce(date)
    Date.validate(date)
    print(f"{date.year} {date.month} {date.day}")
