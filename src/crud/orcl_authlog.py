from datetime import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.oracle_db import orcl_engine
from models.orcl_authlog import OrclAuthLog


def find_logs_with_date(
    date_of: datetime = datetime.today(),
) -> List[OrclAuthLog]:
    """finds the logs with provided date, if no date given in parameter
    then check with current date
    """

    _start_datetime = datetime(
        date_of.year, date_of.month, date_of.day, 00, 00, 00
    )
    _end_datetime = datetime(
        date_of.year, date_of.month, date_of.day, 23, 59, 59
    )

    with Session(orcl_engine, future=True) as session:
        stmt = (
            select(OrclAuthLog)
            .where(OrclAuthLog.transaction_time >= _start_datetime)
            .where(OrclAuthLog.transaction_time < _end_datetime)
        )
        _records = session.execute(stmt)

        return _records.scalars().fetchmany(size=10)


def create_logs(logs: List[OrclAuthLog]):
    with Session(orcl_engine, future=True) as session:
        session.add_all(logs)
        session.commit()
        return True
