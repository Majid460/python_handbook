import threading
import time

from src.remote.weather_alerts_system.services import ServiceAvailability


class AvailabilityBackgroundService:
    def __init__(self, dto_data):
        self.dto_data = dto_data

    def run_availability_service(self):
        service_availability = ServiceAvailability(self.dto_data)
        status = service_availability.check_availability()
        print(f"[Thread] Service status: {status.value}")

    def background_run_availability(self):
        while True:
            self.run_availability_service()
            time.sleep(3)  # run every 3 seconds

    def start_in_thread(self):
        thread = threading.Thread(target=self.background_run_availability, daemon=True)
        thread.start()
        return thread
