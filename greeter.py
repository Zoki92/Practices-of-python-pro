from datetime import datetime


class Greeter:
    def __init__(self, asof, name):
        self._asof = asof
        self.name = name

    def _day(self):
        return self._asof.strftime('%A')

    def _part_of_day(self):
        current_hour = self._asof.hour
        if current_hour < 12:
            return "morning"
        elif 12 <= current_hour < 17:
            return "afternoon"
        else:
            return "evening"

    def greet(self, store):
        print(f"Hi, I'm {self.name} and welcome to {store}")
        print(f"How's your {self._day()} {self._part_of_day()} going?")
        print(f"Here's a coupon for 20% off!")


dtnow = datetime.now()

greeter = Greeter(dtnow, 'Zoran')
greeter.greet('Macedonia')
