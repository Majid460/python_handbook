import json


# Utility class with static method
# Load Data from json file
class LoadDataFromJson:
    @staticmethod
    def load_data():
        try:
            with open("../weather_sample.json", "rt") as f:
                return json.load(f)
        except FileNotFoundError:
            return None


