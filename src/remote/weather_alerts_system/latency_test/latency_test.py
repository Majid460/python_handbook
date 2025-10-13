# Test the latency of api and dto conversion
import time
from dataclasses import dataclass
from enum import Enum
from typing import List, Union

import requests


class ApiParamFilters(Enum):
    USER_ID = "userId"
    ID = "id"
    TITLE = "title"


@dataclass
class Posts:
    userId: int
    id: int
    title: str
    body: str


class LatencyTest:
    def __init__(self):
        self.api_url = "https://jsonplaceholder.typicode.com/posts"
        self.get_latency_wp = None
        self.data = None
        self.data_parsers = DataParsers()

    # Get overall data
    def hit_get_api(self):
        try:
            start = time.perf_counter()
            response = requests.get(self.api_url, timeout=3)
            response.raise_for_status()
            d = self.data_parsers.check_type_of_data(response.json())
            self.data = d
            end = time.perf_counter()  # Time in seconds
            latency = (end - start) * 1000  # convert to ms
            self.get_latency_wp = latency
        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")
            self.get_latency_wp = None
            self.data = None
    @staticmethod
    def make_query_param(filters: dict) -> dict:
        try:
            fil = {}
            for key, val in filters.items():
                match key:
                    case ApiParamFilters.USER_ID if val is not None:
                        fil[ApiParamFilters.USER_ID.value] = val
                    case ApiParamFilters.ID if val is not None:
                        fil[ApiParamFilters.ID.value] = val
                    case ApiParamFilters.TITLE if val is not None:
                        fil[ApiParamFilters.TITLE.value] = val
            return fil
        except Exception as e:
            print(e)

    # Get certain data based on userId
    def get_based_on_filter(self, filters: dict) -> tuple[float, Union[Posts, list[Posts]]]:
        try:
            query = self.make_query_param(filters)
            start_t = time.perf_counter()
            response = requests.get(self.api_url, params=query)
            response.raise_for_status()
            d = self.data_parsers.check_type_of_data(response.json())
            end = time.perf_counter()  # Time in seconds
            latency = (end - start_t) * 1000  # convert to ms
            return latency, d

        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")
            return -1, []


class DataParsers:
    # Parsers
    # Method with the Main Post
    @staticmethod
    def data_parsing(data: dict):
        return Posts(**data)

    # Method without main post
    @staticmethod
    def data_parsing_list(data: List[dict]) -> List[Posts]:
        return [Posts(**obj) for obj in data]

    def check_type_of_data(self, data):
        match data:
            case dict():
                print("data is dict")
                return self.data_parsing(data)
            case list():
                if data is not None:
                    return self.data_parsing_list(data)
            case _:
                print("Data is None")
                return None
