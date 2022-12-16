from database import Base

from .mixins.auth_mixin import StatusMixin
from .mixins.leave_snaction import LeaveSnaction


class OracleLeaveSnaction(LeaveSnaction, StatusMixin, Base):

    __tablename__ = "TB_T_LEAVE_SANCTION"
    __table_args__ = {"schema": "HRMS"}

    def __repr__(self):
        return f"OracleLeaveApplication(LAID={self.LAID},\
            LAEmpCode={self.LSEmpCode},\
                LID={self.LSDate})"


class MSSqlLeaveSnaction(LeaveSnaction, StatusMixin, Base):

    __tablename__ = "TB_T_LEAVE_SANCTION"

    def __repr__(self):
        return f"MSSqlLeaveSnaction(LAID={self.LAID},\
            LAEmpCode={self.LSEmpCode},\
                LID={self.LSDate})"
