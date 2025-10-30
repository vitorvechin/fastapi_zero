from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo!'}


@app.get('/exercicio-aula-02', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def exercicio_aula_02():
    return """
    <html>
        <head>
            <title>Exercício Aula 02</title>
        </head>
        <body>
            <h1>Exercício Aula 02</h1>
            <p>Olá, mundo!</p>
        </body>
    </html>
    """
