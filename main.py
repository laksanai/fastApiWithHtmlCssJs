from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

origins = [
    # "http://localhost:3000",
    # "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="templates")

app.mount("/styles", StaticFiles(directory="styles"), name="styles")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/home", response_class=HTMLResponse)
async def pajt(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=9998, reload=True)