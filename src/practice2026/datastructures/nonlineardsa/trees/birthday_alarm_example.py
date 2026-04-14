"""
A family tree find the upcoming birthday and set alarm

                  Person
                /       \
        Person A        Person B
        /       \       /       \
Person A     Person B  Person A   Person B
"""

from collections import deque
from datetime import date


class Person:
    def __init__(self, name, day, month, parent_one=None, parent_two=None):
        self.name: str = name
        self.day_of_month: int = day
        self.month_of_birthday: int = month
        self.parent_one: Person = parent_one
        self.parent_two: Person = parent_two
        self.alarm_has_set: bool = False

    # For comparison
    def day_month(self):
        return (self.day_of_month, self.month_of_birthday)

    def __str__(self) -> str:
        return (
            f"Person = {self.name}, "
            f"Birthday = {self.day_of_month:02d}/{self.month_of_birthday:02d}, "
            f"Alarm Set = {self.alarm_has_set}"
        )


# Earliest Birthday Finder function
def birthday_finder(p: Person):
    if not p:
        return None
    # I will traverse level by level and find the upcoming birthday
    queue = deque([p])
    min_date_person = (p.day_month(), p)
    while queue:
        curr = queue.popleft()
        # Check if current's date is less than the min_date
        if curr.day_month() < min_date_person[0]:
            min_date_person = (curr.day_month(), curr)
        if curr.parent_one:
            queue.append(curr.parent_one)
        if curr.parent_two:
            queue.append(curr.parent_two)
    return min_date_person[1]


def days_until_birthday(day, month):
    today = date.today()
    curr_year = today.year

    birthday = date(curr_year, month, day)
    # Find the either birthdate has been passed or not
    if birthday < today:
        # if yes then make it for next year
        birthday = date(curr_year + 1, month, day)

    return (birthday - today).days


# Find upcoming birthday
# Upcoming Birthday Finder function
def upcoming_birthday_finder(p: Person):
    if not p:
        return None
    # I will traverse level by level and find the upcoming birthday
    queue = deque([p])
    result = []
    min_days = float("inf")
    while queue:
        curr = queue.popleft()
        d = days_until_birthday(curr.day_of_month, curr.month_of_birthday)
        if d < min_days:
            min_days = d
            result = [curr]  # reset list
        elif d == min_days:
            result.append(curr)  # same date → add
        if curr.parent_one:
            queue.append(curr.parent_one)
        if curr.parent_two:
            queue.append(curr.parent_two)
    return result


# set alarm
def set_alarm(person: Person):
    if person:
        earliest = birthday_finder(person)
        upcoming = upcoming_birthday_finder(person)
        if upcoming:
            for p in upcoming:
                p.alarm_has_set = True
                print(
                    f"⏰ Alarm set Upcoming Birthday {p.name}'s birthday on "
                    f"{p.day_of_month:02d}/{p.month_of_birthday:02d}"
                )

        if earliest or upcoming:
            earliest.alarm_has_set = True
            print(
                f" Earliest birthday's for {earliest.name}'s birthday on {earliest.day_of_month:02d}/{earliest.month_of_birthday:02d}"
            )

        else:
            print("No person found to set alarm for.")


if __name__ == "__main__":
    grand_d = Person("John", 1, 3)
    grand_m = Person("Alexa", 4, 6)
    grand_d_m = Person("James", 1, 4)
    grand_m_m = Person("Jenifer", 4, 6)
    dad = Person("ERIC", 5, 12, grand_d, grand_m)
    mother = Person("Tesa", 6, 11, grand_d_m, grand_m_m)
    me = Person("Stephan", 9, 10, dad, mother)
    set_alarm(me)
