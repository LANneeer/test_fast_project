import os
import aiohttp
from starlette.exceptions import HTTPException
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("API_KEY")


async def get_weather(api_key: str, city: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}") as response:
            data = await response.text()
            data = json.loads(data)
            if response.status > 300:
                raise HTTPException(status_code=response.status, detail=str(data))
            temperature = round(data["main"]["temp"] - 273.15, 1)
            weather_description = data["weather"][0]["description"]
    return {"temperature": temperature, "weather_description": weather_description}
