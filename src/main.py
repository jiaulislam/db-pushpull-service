from datetime import datetime
from pathlib import Path

from crud import push_pull as pp

ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent


if __name__ == "__main__":

    today = datetime.today()

    _start_datetime = datetime(today.year, today.month, today.day, 0, 0, 0)

    _end_datetime = datetime(today.year, today.month, today.day, 23, 59, 59)

    # create the logs from sql server to oracle
    pp.core_create_logs(_start_datetime, _end_datetime)

    # update the logs on both sql server and oracle
    pp.core_update_logs(_start_datetime, _end_datetime, 100)

    # pull the leave application table
    pp.etl_tbl_t_leave_application()

    # pull the employee leave application table
    pp.etl_tbl_t_emp_leave_application()

    # pull the leave snaction table
    pp.etl_tb_t_leave_sanction()
