from pydantic import BaseModel


class IndexModel(BaseModel):
    index_key: int

    class Config:
        orm_mode = True
