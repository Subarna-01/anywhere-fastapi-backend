from pydantic import BaseModel, EmailStr
from datetime import date

class EmailRequestSchema(BaseModel):
    customer_name: str
    customer_email: EmailStr
    customer_phone: str
    tour_package_name: str
    tour_start_date: date
