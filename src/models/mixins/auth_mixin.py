from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class AuthLogMixin:
    index_key = Column(
        "indexkey", Integer, nullable=False, index=True, primary_key=True
    )
    user_id_index = Column("useridindex", Integer)
    user_id = Column("userid", String(30))
    transaction_time = Column("transactiontime", DateTime)
    terminal_id = Column("terminalid", Integer)
    auth_type = Column("authtype", Integer)
    auth_result = Column("authresult", Integer)
    function_key = Column("functionkey", Integer)
    server_record_time = Column("serverrecordtime", DateTime)
    reserved = Column("reserved", Integer)
    log_type = Column("logtype", Integer)
    temp_value = Column("tempvalue", Integer)
    min_index = Column("minindex", Integer)


@declarative_mixin
class StatusMixin:
    status = Column("pushstat", Integer)
