from datetime import datetime

from pydantic import BaseModel


class AuthLogBase(BaseModel):
    index_key: int
    user_id_index: int
    user_id: str | None
    transaction_time: datetime
    terminal_id: int | None
    auth_type: int | None
    auth_result: int | None
    function_key: int | None
    server_record_time: datetime | None
    reserved: int | None
    log_type: int | None
    temp_value: int | None
    min_index: int | None

    class Config:
        orm_mode = True


class MSqlAuthLog(AuthLogBase):
    status: int
