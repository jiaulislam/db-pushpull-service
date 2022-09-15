from datetime import datetime

from pydantic import BaseModel


class AuthLogBase(BaseModel):
    index_key: int
    user_id_index: int
    user_id: str
    transaction_time: datetime
    terminal_id: int
    auth_type: int
    auth_result: int
    function_key: int
    server_record_time: datetime
    reserved: int
    log_type: int
    temp_value: int
    min_index: int

    class Config:
        orm_mode = True


class MSqlAuthLog(AuthLogBase):
    status: int
