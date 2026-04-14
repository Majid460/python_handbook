from collections import deque


class Person:
    def __init__(self, name, day, month, person_a=None, person_b=None):
        self.name: str = name
        self.day_of_month: int = day
        self.month_of_birthday: int = month
        self.person_a: Person = person_a
        self.person_b: Person = person_b
        self.alarm_has_set: bool = False

    def day_month_finder(self):
        return self.day_of_month, self.month_of_birthday

    def __str__(self):
        return (
            f"Person = {self.name}, "
            f"Birthday = {self.day_of_month:02d}/{self.month_of_birthday:02d}, "
            f"Alarm Set = {self.alarm_has_set}"
        )


# Find the earliest birthday
def find_birthday(root):
    earliest = root
    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if temp.day_month_finder() < earliest.day_month_finder():
            earliest = temp
        if temp.person_a:
            queue.append(temp.person_a)
        elif temp.person_b:
            queue.append(temp.person_b)
    return earliest


# set alarm
def set_alarm(person: Person):
    if person:
        earliest = find_birthday(person)
        if earliest:
            earliest.has_alarm = True
            print(
                f"⏰ Alarm set for {earliest.name}'s birthday on {earliest.day_of_month:02d}/{earliest.month_of_birthday:02d}"
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
