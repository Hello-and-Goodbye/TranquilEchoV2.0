from pydantic import BaseModel
class Token(BaseModel):
    access_token: str
    token_type: str
class Guest(BaseModel):
    guest_bool:bool
class Therapist(BaseModel):
    username:str
    password:str
    email:str
    full_name:str
    phone_number:str
    title:str
    description:str
    age:int
    qualification:str
    is_active:bool
    cases:str
    history:str
    gender:str
class Message(BaseModel):
    content:str
    history:str
    date:str
    message_type:str
    user_id:int
    thread_id:int
    id:int
    keywords:str
class User(BaseModel):
    username:str
    password:str
    email:str
    full_name:str
    phone_number:str
    description:str
    history:str
    social_media:str
    is_active:bool
    age:int  
    gender:str
    is_staff:bool
    job_title:str
    is_superuser:bool
    level:int
    index:int




