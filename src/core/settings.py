from pydantic import BaseSettings
from sqlalchemy.engine import URL


class Settings(BaseSettings):

    oracle_db_username: str
    oracle_db_password: str
    oracle_db_host: str
    oracle_db_port: str
    oracle_db_name: str
    oracle_db_driver: str
    oracle_tbl_name: str
    oracle_schema_name: str

    mssql_db_username: str
    mssql_db_password: str
    mssql_db_host: str
    mssql_db_port: str
    mssql_db_name: str
    mssql_db_driver: str
    mssql_tbl_name: str

    mssql_206_db_username: str
    mssql_206_db_password: str
    mssql_206_db_host: str
    mssql_206_db_port: str
    mssql_206_db_name: str
    mssql_206_db_driver: str
    mssql_206_tbl_name: str

    def get_oracle_dsn(self) -> URL:
        return URL.create(
            f"oracle+{self.oracle_db_driver}",
            username=self.oracle_db_username,
            password=self.oracle_db_password,
            host=self.oracle_db_host,
            port=self.oracle_db_port,
            database=self.oracle_db_name,
        )

    def get_mssql_dsn(self) -> URL:
        return URL.create(
            f"mssql+{self.mssql_db_driver}",
            username=self.mssql_db_username,
            password=self.mssql_db_password,
            host=self.mssql_db_host,
            port=self.mssql_db_port,
            database=self.mssql_db_name,
            query={
                "driver": "ODBC Driver 18 for SQL Server",
                "TrustServerCertificate": "yes",
            },
        )

    def get_mssql_dsn_206(self) -> URL:
        return URL.create(
            f"mssql+{self.mssql_206_db_driver}",
            username=self.mssql_206_db_username,
            password=self.mssql_206_db_password,
            host=self.mssql_206_db_host,
            port=self.mssql_206_db_port,
            database=self.mssql_206_db_name,
            query={
                "driver": "ODBC Driver 18 for SQL Server",
                "TrustServerCertificate": "yes",
            },
        )

    class Config:
        env_file = ".env"


config = Settings()
