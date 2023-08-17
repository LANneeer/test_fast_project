from fastapi import FastAPI
from utils.email import EmailService, email_conf, EmailSchema
from utils.weather import get_weather, api_key

app = FastAPI()


# Email sending gateway
@app.post("/send_email/")
async def send_email(email: EmailSchema, message: str):
    client = EmailService(conf=email_conf)
    response = await client.send_mail(email=email, message=message)
    return response


# Weather in Moscow gateway
@app.get("/weather/{city}/")
async def get_weather_moscow(city: str):
    response = await get_weather(api_key=api_key, city=city)
    return response


# Array sorting gateway
@app.post("/sort_array/")
async def sort_array(array: list[int]):
    sorted_array = sorted(array)
    return {"sorted_array": sorted_array}
