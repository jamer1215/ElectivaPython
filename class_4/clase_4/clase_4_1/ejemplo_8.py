import time
from pydantic import BaseModel, Field
from datetime import datetime

class Blog(BaseModel):
    title: str 
    created_at: datetime = Field(default_factory=datetime.now)#Cada vez que crees una instancia nueva, ejecutá datetime.now() en ese momento
    is_active: bool

print(Blog(title="Our First Blog",is_active=True))

time.sleep(5)

print(Blog(title="Our Second Blog",is_active=True))