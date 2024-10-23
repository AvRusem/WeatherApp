# WeatherApp

## How to run

1. Get API key from [AccuWeather](https://developer.accuweather.com/accuweather-forecast-api/apis). Sign up then create an app (select Core Weather Limited Trial and None in MinuteCast) and finally you will get a key.

2. Create .env in service/ and copy this into it
   ```
   API_KEY=<Your API key>
   ```

3. Now you have 2 options how to run an app

   ### Local

   ```
   pip3 install -r requirements.txt &&
   python3 service/service.py
   ```

   ### docker-compose

   ```
   docker-compose up --build
   ```
