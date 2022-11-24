from pydantic import BaseModel


class Player(BaseModel):
    name: str
    user_id: str
