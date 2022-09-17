import time
from datetime import datetime

from sqlalchemy import bindparam, insert, select, update
from sqlalchemy.orm import Session

from database.mssql_db import mssql_engine
from database.oracle_db import orcl_engine
from models.mssql_authlog import MsSqlAuthLog as MAuthModel
from models.orcl_authlog import OrclAuthLog as OAuthModel


def core_create_logs(
    start_time: datetime, end_time: datetime, yield_range: int = 1000
) -> None:
    mssql_select_stmt = (
        select(MAuthModel)
        .where(MAuthModel.transaction_time >= start_time)
        .where(MAuthModel.transaction_time < end_time)
        .where(MAuthModel.user_id != None)  # noqa
        .where(MAuthModel.status == None)  # noqa
    )

    # Pull from Database
    with Session(orcl_engine, future=True) as orcl_session:
        # Transaction Begin
        with orcl_session.bind.begin() as orcl_connection:
            with mssql_engine.connect() as mysql_connection:
                t0 = time.time()
                _total_inserted: int = 0
                # get a cursor of 1000 at a time
                cursor = mysql_connection.execution_options(
                    yield_per=1000
                ).execute(mssql_select_stmt)

                # loop through the cursor partitions to fetch data
                for partition in cursor.partitions():
                    # insert all 1000 data in executemany mode
                    t1 = time.time()
                    res = orcl_connection.execute(
                        insert(OAuthModel), [dict(row) for row in partition]
                    )
                    _total_inserted += res.rowcount
                    print(
                        f"{res.rowcount} Records Took: \
                            {time.time() - t1:.3f} secs"
                    )
                # Transaction End
                orcl_connection.commit()
                print(
                    f"Total: {_total_inserted} Records Took: \
                        {time.time() - t0:.3f} secs"
                )


def core_update_logs(
    start_date: datetime, end_date: datetime, yield_range: int = 1000
) -> None:

    orcl_select_stmt = (
        select(OAuthModel)
        .where(OAuthModel.status == None)  # noqa
        .where(OAuthModel.transaction_time >= start_date)
        .where(OAuthModel.transaction_time < end_date)
    )

    mssql_update_stmt = (
        update(MAuthModel)
        .where(MAuthModel.index_key == bindparam("indexKey"))
        .values(pushstat=1)  # noqa
    )

    orcl_update_stmt = (
        update(OAuthModel)
        .where(OAuthModel.index_key == bindparam("indexKey"))
        .values(pushstat=1)  # noqa
    )

    # Update into Microsoft SQL Server
    with mssql_engine.connect() as mssql_conn:
        with orcl_engine.connect() as orcl_conn:
            t0 = time.time()
            cursor = orcl_conn.execution_options(
                yield_par=yield_range
            ).execute(orcl_select_stmt)
            _total_sent = 0
            for partition in cursor.partitions():
                t1 = time.time()
                _total_sent += len(partition)

                # update in mysql server
                if len(partition):
                    mssql_conn.execute(
                        mssql_update_stmt,
                        [{"indexKey": row[0]} for row in partition],
                    )
                    print(
                        f"My SQL Server Record: {len(partition)}\
                            Updated In : {time.time() - t1:.3f} secs"
                    )
                t2 = time.time()
                # update in orcl server
                if len(partition):
                    orcl_conn.execute(
                        orcl_update_stmt,
                        [{"indexKey": row[0]} for row in partition],
                    )
                    print(
                        f"Oracle Server Record: {len(partition)}\
                            Updated In : {time.time() - t2:.3f} secs"
                    )
            orcl_conn.commit()
            mssql_conn.commit()
            print(
                f"Total Record:{_total_sent}\
                    Updated In: {time.time() - t0:.3f} secs"
            )
