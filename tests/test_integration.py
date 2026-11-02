import pytest
import json
from pathlib import Path
from app.integrations.open_meteo import parse_weather

MOCK_FILE = Path(__file__).parent/"mock"/"mock.json"

def load_mock_data():
    with open(MOCK_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def test_load_mock_json():
    data=load_mock_data()

    assert isinstance(data, dict)
    assert "longitude" in data
    assert "latitude" in data
    assert "current" in data


def test_parse_weather():
    mock_data = load_mock_data()
    result = parse_weather(mock_data)
    assert result["latitude"] == -6.2088
    assert result["longitude"] == 106.8456
    assert result["temperature"] == 29.5
    assert result["humidity"] == 75
    assert result["precipitation"] == 0.2
    assert result["wind_speed"] == 12.5
    assert result ["weather_code"] == 61