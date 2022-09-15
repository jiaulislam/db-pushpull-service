from datetime import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.mssql_db import mssql_engine
from models.mssql_authlog import MsSqlAuthLog


def find_logs_with_date(
    date_of: datetime = datetime.today(),
) -> List[MsSqlAuthLog]:
    """finds the logs with provided date, if no date given in parameter
    then check with current date
    """

    _start_datetime = datetime(
        date_of.year, date_of.month, date_of.day, 00, 00, 00
    )
    _end_datetime = datetime(
        date_of.year, date_of.month, date_of.day, 23, 59, 59
    )

    with Session(mssql_engine, future=True) as session:
        stmt = (
            select(MsSqlAuthLog)
            .where(MsSqlAuthLog.transaction_time >= _start_datetime)
            .where(MsSqlAuthLog.transaction_time < _end_datetime)
            .where(MsSqlAuthLog.status == None)  # noqa
        )
        _records = session.execute(stmt)

        return _records.scalars().fetchmany(10)


def update_log_share_status(index_key: int):
    """update the share status of sql server success(1)
    relative to index_key
    """
    with Session(mssql_engine, future=True) as session:
        stmt = select(MsSqlAuthLog).where(MsSqlAuthLog.index_key == index_key)
        _record = session.scalars(stmt).one()
        _record.status = 1
        session.execute(stmt)
        session.commit()
        return True
