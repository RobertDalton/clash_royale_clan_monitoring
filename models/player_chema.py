from pydantic import BaseModel

class ClanParticipant(BaseModel):
    name: str
    fame: int 
    decksUsed: int 
    decksUsedToday: int 
