from functions import *

import json


def test_IsWeatherGood():
    assert IsWeatherGood(0, 30, 50, 10) == True
    assert IsWeatherGood(-1, 30, 50, 10) == False
    assert IsWeatherGood(0, 29, 50, 10) == False
    assert IsWeatherGood(35, 60, 30, 11) == True
    assert IsWeatherGood(36, 30, 50, 10) == False
    assert IsWeatherGood(20, 61, 50, 10) == False
    assert IsWeatherGood(20, 50, 51, 10) == False
    assert IsWeatherGood(20, 50, 20, 9) == False
    assert IsWeatherGood(20, 50, 20, 20) == True


def test_Parse():
    data = '''
    {
    "LocalObservationDateTime": "2024-10-23T21:21:00+03:00",
    "EpochTime": 1729707660,
    "WeatherText": "Cloudy",
    "WeatherIcon": 7,
    "HasPrecipitation": false,
    "PrecipitationType": null,
    "IsDayTime": false,
    "Temperature": {
        "Metric": {
            "Value": 8.0,
            "Unit": "C",
            "UnitType": 17
        },
        "Imperial": {
            "Value": 46.0,
            "Unit": "F",
            "UnitType": 18
        }
    },
    "RealFeelTemperature": {
        "Metric": {
            "Value": 0.0,
            "Unit": "C",
            "UnitType": 17,
            "Phrase": "Cold"
        },
        "Imperial": {
            "Value": 32.0,
            "Unit": "F",
            "UnitType": 18,
            "Phrase": "Cold"
        }
    },
    "RelativeHumidity": 89,
    "IndoorRelativeHumidity": 41,
    "DewPoint": {
        "Metric": {
            "Value": 6.3,
            "Unit": "C",
            "UnitType": 17
        },
        "Imperial": {
            "Value": 43.0,
            "Unit": "F",
            "UnitType": 18
        }
    },
    "Wind": {
        "Direction": {
            "Degrees": 270,
            "Localized": "W",
            "English": "W"
        },
        "Speed": {
            "Metric": {
                "Value": 34.4,
                "Unit": "km/h",
                "UnitType": 7
            },
            "Imperial": {
                "Value": 21.4,
                "Unit": "mi/h",
                "UnitType": 9
            }
        }
    },
    "UVIndex": 0,
    "UVIndexText": "Low",
    "Visibility": {
        "Metric": {
            "Value": 22.5,
            "Unit": "km",
            "UnitType": 6
        },
        "Imperial": {
            "Value": 14.0,
            "Unit": "mi",
            "UnitType": 2
        }
    }
    }
'''
    data = json.loads(data)

    dict_data = Parse(data)
    assert dict_data['temperature'] == 8
    assert dict_data['humidity'] == 89
    assert dict_data['wind_speed'] == 34.4
    assert dict_data['visibility'] == 22.5
