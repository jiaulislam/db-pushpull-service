from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class LeaveApplication:
    LAID = Column("laid", Integer, primary_key=True)
    LAEmpCode = Column("laempcode", String(6))
    LID = Column("lid", Integer)
    LAApplFormNo = Column("laapplformno", String(25))
    LAApplFormDate = Column("laapplformdate", DateTime)
    LAPurpose = Column("lapurpose", String(250))
    LAFrmDt = Column("lafrmdt", DateTime)
    LAEndDt = Column("laenddt", DateTime)
    LAHalf = Column("lahalf", Integer)
    LANOOFDAYS = Column("lanoofdays", Float(2))
    LAStatus = Column("lastatus", Integer)
    LAStaOn = Column("lastaon", DateTime)
    LABALANCE = Column("labalance", Float(2))
    CrtBy = Column("crtby", String(20))
    CrtOn = Column("crton", DateTime)


@declarative_mixin
class EmpLeaveApplication:
    SandToEmpCode = Column("sandtoempcode", String(6), nullable=False)
