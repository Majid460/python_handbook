from dataclasses import dataclass
from typing import List, Dict

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Coord:
    lat: float
    lon: float
@dataclass_json
@dataclass
class Weather:
    id: int
    main: str
    description: str
    icon: str
@dataclass_json
@dataclass
class Main:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
@dataclass_json
@dataclass
class Wind:
    speed: float
    deg: int
    gust: float
@dataclass_json
@dataclass
class Clouds:
    all: int

@dataclass_json
@dataclass
class Rain:
    amounts: Dict[str, float]
@dataclass_json
@dataclass
class Sys:
    country: str
    sunrise:int
    sunset:int

@dataclass_json
@dataclass
class WeatherResponse:
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: float
    wind: Wind
    clouds: Clouds
    rain: Rain
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int

