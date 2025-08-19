from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorData(BaseModel):
    carVal: float

latest_data = None

@app.post("/")
async def sensor_data(data: SensorData):
    global latest_data
    latest_data = data.carVal
    return {"status":"success"}

@app.get("/")
async def dashboard():
    return {"carVal": latest_data} 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)