import os
import aiohttp
from starlette.exceptions import HTTPException

api_key = os.getenv("API_KEY")


async def get_weather(api_key: str, city: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}") as response:
            data = await response.text()
            if response.status > 300:
                raise HTTPException(status_code=response.status, detail=str(data))
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]
    return {"temperature": temperature, "weather_description": weather_description}
