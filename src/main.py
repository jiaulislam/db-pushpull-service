from datetime import datetime
from pathlib import Path
from typing import List

from crud import mssql_authlog as MAuthCrud
from crud import orcl_authlog as OAuth
from models.orcl_authlog import OrclAuthLog as OAuthModel
from service import auth_log_service as AuthService

ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent


if __name__ == "__main__":

    ms_auth_data = MAuthCrud.find_logs_with_date(
        datetime(2022, 9, 14, 00, 00, 00)
    )

    _list: List[OAuthModel] = list(
        map(
            AuthService.convert_to_oauthlog_model,
            list(map(AuthService.convert_to_authlog_schema, ms_auth_data)),
        )
    )

    OAuth.create_logs(_list)
