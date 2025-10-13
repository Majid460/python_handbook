# In this service we will check the availability of service
from enum import EnumType, Enum

from src.remote.weather_alerts_system.data.model import WeatherResponse

class ServiceStatus(Enum):
    SERVICE_DOWN = "Service is down"
    SERVICE_UP = "Service is up"
    SERVICE_CRASHED = "Service is crashed"


# Check if code is not 200 means service is not available
class ServiceAvailability:

    def __init__(self, data):
        self._data: WeatherResponse = data

    @property
    def data_to(self):
        return self._data

    @data_to.setter
    def data_to(self, data: WeatherResponse):
        if data:
            self._data = data
        else:
            raise ValueError("Data required")

    # Check the code
    def check_availability(self):
        try:
            if self._data.cod != 200:
                return ServiceStatus.SERVICE_DOWN
            else:
                return ServiceStatus.SERVICE_UP
        except Exception as e:
            print(f"Error:: {e} ")
            return ServiceStatus.SERVICE_CRASHED
