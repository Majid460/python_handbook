from dataclasses import dataclass
from pathlib import Path
import csv
from typing import List


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    city: str
    occupation: str


class CSVData:
    def __init__(self) -> None:
        self.data: List[Person] = []

    def load_data(self):

        # Path - Use relative-to-script path (dynamic absolute)
        # Easy to find files from any directory
        try:
            file_path = Path(__file__).parent / "data.csv"

            with open(file_path, "r") as f:
                # Read using csv reader as dict
                reader = csv.DictReader(
                    f
                )  # It reads each row of CSV as a dictionary instead of a list
                for row in reader:
                    # convert types important
                    person = Person(
                        name=row["name"],
                        age=int(row["age"]),
                        city=row["city"],
                        occupation=row["occupation"],
                    )
                    self.data.append(person)
            # raise Exception("Error")
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            print(e)
            return None

    def get_age_greater_than(self, age):
        # [person for person in self.data if person["age"] > age] # Without data modeling
        return [person for person in self.data if person.age > age]

    def get_by_city(self, city):
        # [person for person in self.data if person["city"] == city]
        return [person for person in self.data if person.city == city]

    def get_names(self):
        return [person.name for person in self.data]


if __name__ == "__main__":
    # 1. Load data from csv
    csvData = CSVData()
    csvData.load_data()

    # Get data where age is greater than
    print(f"Age Greater than: {csvData.get_age_greater_than(30)}")

    # Get data where city is equal to
    print(f'City equal to: {csvData.get_by_city("Chicago")}')
    # City equal to: [{'name': 'Carol', 'age': 42, 'city': 'Chicago', 'occupation': 'Project Manager'}]

    # Get names only
    print(f"Get names: {csvData.get_names()}")
    # Get names: ['Alice', 'Bob', 'Carol', 'David', 'Eve']


# To read excel file

# 1. Use pandas
# import pandas as pd

# df = pd.read_excel("data.xlsx")

# print(df)

# 2. Use openpyxl more low leve

# from openpyxl import load_workbook

# def load_people():
#     wb = load_workbook("data.xlsx")
#     sheet = wb.active

#     people = []

#     rows = list(sheet.iter_rows(values_only=True))
#     headers = rows[0]

#     for row in rows[1:]:
#         data = dict(zip(headers, row))

#         person = Person(
#             name=data["name"],
#             age=int(data["age"]),
#             city=data["city"],
#             occupation=data["occupation"]
#         )
#         people.append(person)

#     return people
