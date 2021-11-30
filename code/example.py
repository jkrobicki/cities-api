from fastapi import FastAPI, Form
from typing import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/message/")
async def read_message():
    return """
        <html>
            <head>
              <h2>Welcome to cities-app!</h2>
            </head>
        </html>
        """
