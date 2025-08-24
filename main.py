from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.mail.router import mail_router

app = FastAPI(title='Anywhere FastAPI APIs v1.0.0')

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(mail_router)

