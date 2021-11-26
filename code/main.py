from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form
import dominate
from dominate.tags import *


class City(BaseModel):
    city_name: str
    why_answer: Optional[str] = None


app = FastAPI()


@app.get("/message/", response_class=HTMLResponse)
async def read_message():
    print("works")
    _html = html()
    _head, _body = _html.add(head(title("Cities")), body())
    _body.add(h2("What is your favorite city?"))
    _form = _body.add(form(action="/city_name", method="post"))
    _label = label("City name:", fr="cname")
    _input1 = input_(type="text", id="cname", name="cname")
    _input2 = input_(type="submit", value="Submit")
    _form.add(_label, _input1, _input2)
    return _html.render()

    # return """
    # <html>
    #     <head>
    #         <title>Cities</title>
    #     </head>
    #     <body>
    #         <h2>What is your favorite city?</h2>
    #         <form action="/city_name" method="post">
    #             <label for="cname">City name:</label>
    #             <input type="text" id="cname" name="cname"><br><br>
    #             <input type="submit" value="Submit">
    #         </form>
    #     </body>
    # </html>
    # """


@app.post("/city_name/", response_class=HTMLResponse)
async def login(cname: str = Form(...)):
    print(cname)
    return f"""
    <html>
        <head>
            <title>Cities</title>
        </head>
        <body>
            <h1>Are you sure {cname} is your favorite city?</h1>
        </body>
    </html>
    """
