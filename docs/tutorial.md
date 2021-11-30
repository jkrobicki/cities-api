Your main focus will be orbiting around API framework, with python code as its backbone.  

### 1)    First steps  
Your first task is to create new file in python with fastAPI framework.  
If lost, you can also search for an answer on [fastAPI documentation page](https://fastapi.tiangolo.com/).

* install fastAPI
```bash
pip install fastapi
```
* You will also need an ASGI server (uvicorn)
```bash
pip install "uvicorn[standard]"
```
* in folder "cities" create new file "main.py"   with:
```bash
from typing import Optional

from fastapi import FastAPI


app = FastAPI()


@app.get("/message/", response_class=HTMLResponse)
async def read_message():
    return """
        <html>
            <head>
              <h2>Welcome to cities-app!</h2>
            </head>
        </html>
        """

```

- You already created an API that:  
    - Receives HTTP request in the path /message/
    - The path takes GET operation (an HTTP method)
    - server returns JSON response

### Task:  
- By default, FastAPI will return the responses using JSONResponse. With [fastAPI docs](https://fastapi.tiangolo.com/) try to find out how to return a HTML response and implement it in the code