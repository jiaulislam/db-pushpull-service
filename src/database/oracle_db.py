from sqlalchemy import create_engine

from core.settings import config as conf

orcl_engine = create_engine(conf.get_oracle_dsn(), future=True)
