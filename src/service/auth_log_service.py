from models.mssql_authlog import MsSqlAuthLog as MAuthModel
from models.orcl_authlog import OrclAuthLog as OAuthModel
from schemas.auth_log import AuthLogBase
from schemas.utils import IndexModel


def convert_to_authlog_schema(auth_log: MAuthModel) -> AuthLogBase:
    return AuthLogBase.from_orm(auth_log)


def convert_to_oauthlog_model(log: AuthLogBase) -> OAuthModel:
    return OAuthModel(**log.dict())


def parse_index_key(oAuth: MAuthModel):
    return IndexModel.from_orm(oAuth)


def serialize_index_key(log: IndexModel):
    return log.dict()
