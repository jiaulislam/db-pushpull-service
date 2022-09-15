from core.settings import config as _conf
from database import Base

from .mixins.auth_mixin import AuthLogMixin


class OrclAuthLog(AuthLogMixin, Base):

    __tablename__ = _conf.oracle_tbl_name
    __table_args__ = {"schema": _conf.oracle_schema_name}

    def __repr__(self):
        return f"OAuthLog(IndexKey={self.index_key},\
            UserIdIndex={self.user_id_index},\
                UserId={self.user_id},\
                    TransactionTime={self.transaction_time})"
