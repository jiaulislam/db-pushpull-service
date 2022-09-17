from datetime import datetime
from pathlib import Path

from crud import push_pull as pp

ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent


if __name__ == "__main__":

    today = datetime.today()

    _start_datetime = datetime(today.year, today.month, today.day, 0, 0, 0)

    _end_datetime = datetime(today.year, today.month, today.day, 23, 59, 59)

    pp.core_create_logs(_start_datetime, _end_datetime)
    pp.core_update_logs(_start_datetime, _end_datetime, 100)
