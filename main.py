from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  # <-- Import this
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Mount the static directory.
# This tells FastAPI: "Any request to the path /static should serve files from the 'static' folder."
app.mount("/static", StaticFiles(directory="static"), name="static")

# This sets up the templating engine to look in the "templates" folder
templates = Jinja2Templates(directory="templates")

# ... (keep your CORS, Pydantic model, and endpoints the same) ...
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorData(BaseModel):
    carVal: float

latest_data = None

@app.post("/")
async def receive_sensor_data(data: SensorData):
    global latest_data
    latest_data = data.carVal
    return {"status": "success", "received_value": data.carVal}

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)