from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
async def not_timed():
    return {"message": "This changed now - December 2022"}

    
