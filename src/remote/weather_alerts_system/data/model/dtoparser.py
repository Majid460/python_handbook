from src.remote.weather_alerts_system.data.model import WeatherResponse, Coord, Weather, Main, Wind, Clouds, Rain, Sys


# DTO class to convert the weather data from json to models
class ParseDataToDTO:
    # Parse using json from_dict method
    @staticmethod
    def parse_data(data):
        try:
            if "rain" in data:
                data["rain"] = {"amounts": data["rain"]}
            return WeatherResponse.from_dict(data)
        except Exception as e:
            print("Error parsing data:", e)

    # Parse using general way
    @staticmethod
    def parse_data_gen(data: dict) -> WeatherResponse:
        return WeatherResponse(
            coord=Coord(**data.get("coord")) if data.get("coord") else None,  # ** used to unpack the dict
            weather=[Weather(**w) for w in data.get("weather", []) or []],
            base=data.get("base", None),
            main=Main(**data.get("main")) if data.get("main") else None,
            visibility=data.get("visibility", None),
            wind=Wind(**data.get("wind")) if data.get("wind") else None,
            clouds=Clouds(**data.get("clouds")) if data.get("clouds") else None,
            rain=Rain(amounts=data["rain"]["amounts"]) if (
                    data.get("rain") and "amounts" in data["rain"]
            ) else None,
            sys=Sys(**data.get("sys")) if data.get("sys") else None,
            timezone=data.get("timezone"),
            id=data.get("id"),
            name=data.get("name"),
            cod=data.get("cod"),
        )
