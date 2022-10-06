from fastapi import FastAPI, Request
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="client/build/static"), name="static")

templates = Jinja2Templates(directory="client/build")


@app.get("/{full_path:path}")
async def serve_react_app(request: Request, full_path: str):
    """Serve the react app
    `full_path` variable is necessary to serve each possible endpoint with
    `index.html` file in order to be compatible with `react-router-dom
    """
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
