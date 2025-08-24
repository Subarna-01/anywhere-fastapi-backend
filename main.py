from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from modules.mail.router import mail_router

app = FastAPI(title='Anywhere FastAPI APIs v1.0.0')

origins = ['*']

@app.get('/')
async def get_root() -> dict:
    return {
        'msg': 'Hello World',
        'status_code': status.HTTP_200_OK
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(mail_router)

