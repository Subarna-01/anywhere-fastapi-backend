import os
from dotenv import load_dotenv
from fastapi import Response, status
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from modules.mail.schema import EmailRequestSchema

load_dotenv()

class MailService:
    def __init__(self) -> None:
        self.conf = ConnectionConfig(
            MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
            MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
            MAIL_FROM=os.getenv('MAIL_FROM'),
            MAIL_FROM_NAME=os.getenv('MAIL_FROM_NAME'),
            MAIL_PORT=int(os.getenv('MAIL_PORT')),
            MAIL_SERVER=os.getenv('MAIL_SERVER'),
            MAIL_STARTTLS=True,
            MAIL_SSL_TLS=False,
            USE_CREDENTIALS=True,
            TEMPLATE_FOLDER=os.path.join(os.getcwd(), 'modules', 'mail', 'templates')
        )

    async def send(self, res: Response, req_body: EmailRequestSchema) -> dict:
        recipients = os.getenv('MAIL_RECIPIENTS', '')
        cc = os.getenv('MAIL_CC', '')

        recipient_list = [email.strip() for email in recipients.split(',') if email.strip()]
        cc_list = [email.strip() for email in cc.split(',') if email.strip()]

        try:            
            message = MessageSchema(
                subject='Booking Request',
                recipients=recipient_list,  
                cc=cc_list, 
                template_body={
                    'customer_name': req_body.customer_name,
                    'customer_email': req_body.customer_email,
                    'customer_phone': req_body.customer_phone,
                    'tour_package_name': req_body.tour_package_name,
                    'tour_start_date': req_body.tour_start_date.strftime('%d/%m/%Y')
                },
                subtype=MessageType.html
            )

            fm = FastMail(self.conf)
            await fm.send_message(message, template_name='booking_request.html')

            res.status_code = status.HTTP_200_OK
            return {
                'msg': 'Email sent successfully',
                'status_code': status.HTTP_200_OK
            }

        except Exception as err:
            res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {
                'msg': 'An unexpected error has occurred',
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'error_detail': str(err)
            }
