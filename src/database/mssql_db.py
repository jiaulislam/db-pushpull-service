from sqlalchemy import create_engine

from core.settings import config as conf

mssql_engine = create_engine(conf.get_mssql_dsn(), future=True)

mssql_engine_206 = create_engine(conf.get_mssql_dsn_206(), future=True)
