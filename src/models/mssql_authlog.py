from core.settings import config as _conf
from database import Base

from .mixins.auth_mixin import AuthLogMixin, StatusMixin


class MsSqlAuthLog(AuthLogMixin, StatusMixin, Base):
    __tablename__ = _conf.mssql_tbl_name

    def __repr__(self):
        return f"MSAuthLog(IndexKey={self.index_key},\
            UserIdIndex={self.user_id_index},\
                UserId={self.user_id},\
                    TransactionTime={self.transaction_time})"
