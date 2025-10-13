import threading
import time

from src.remote.weather_alerts_system.core.availability_task import AvailabilityBackgroundService
from src.remote.weather_alerts_system.data.model.dtoparser import ParseDataToDTO
from src.remote.weather_alerts_system.data.load.loads_data import LoadDataFromJson
from src.remote.weather_alerts_system.latency_test.latency_test import LatencyTest, ApiParamFilters


def availability_thread(dto):
    service = AvailabilityBackgroundService(dto)
    # Run service in background thread
    service.start_in_thread()


if __name__ == '__main__':
    # Load data from json and use it
    # Call the static method of utility class defined
    data = LoadDataFromJson.load_data()
    # Pass the json data to parse function to get the modeled data
    dto = ParseDataToDTO.parse_data(data)
    dto_gen = ParseDataToDTO.parse_data_gen(data)
    print(dto)
    print("\n-----------------Gen DTO -----------------")
    print(dto_gen)
    print("\n-----------------Service availability -----------------")
    # Service availability
    availability_thread(dto_gen)
    print("\n-----------------Latency Check -----------------")
    latency_check = LatencyTest()
    latency_check.hit_get_api()
    print(latency_check.data)
    print(f"Latency is:: {latency_check.get_latency_wp} ms")
    print("\n-----------------Get Api data of user -----------------")
    query = {ApiParamFilters.ID:1}
    latency, data = latency_check.get_based_on_filter(query)
    print(f"Latency: {latency:.2f} ms")
    if isinstance(data, list):
        [print(obj) for obj in data]
