from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder
from modules.mail.schema import EmailRequestSchema
from modules.mail.services import MailService

mail_router = APIRouter(prefix='/mail')

mail_service = MailService()

@mail_router.post('/send')
async def send(res: Response, req_body: EmailRequestSchema) -> dict:
    response = await mail_service.send(res, req_body)
    return jsonable_encoder(response)