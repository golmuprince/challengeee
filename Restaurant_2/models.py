from pydantic import BaseModel
from typing import Optional

class UserAccountContext(BaseModel):
    name: Optional[str] = None
    menu: Optional[str] = None
    allergy: Optional[str] = None
    date: Optional[str] = None
    email: Optional[str] = None


class InputGuardRailOutput(BaseModel):
    
    is_off_topic: bool
    reason: str
     
class HandoffData(BaseModel):
    to_agent_name : str

