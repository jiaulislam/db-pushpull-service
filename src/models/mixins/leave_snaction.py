from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class LeaveSnaction:
    LSID = Column("lsid", Integer, primary_key=True)
    LAID = Column("laid", Integer, primary_key=True)
    LSEmpCode = Column("lsempcode", String(6))
    LSDate = Column("lsdate", DateTime)
    LSRemarks = Column("lsremarks", String(200))
    CrtBy = Column("crtby", String(20))
    CrtOn = Column("crton", DateTime)
    ApproveRemarks = Column("approveremarks", String(500))
    SanctBy = Column("sanctby", String(6))
