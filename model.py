from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID,uuid4
from enum import Enum
class Genders(str,Enum):
    male='male'
    female='female'
    
class Role(str,Enum):
    admin='admin'
    user='user'
    studnet='student'

class User(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:str
    last_name:str
    middle_name:str
    gender:Genders
    role:List[Role]