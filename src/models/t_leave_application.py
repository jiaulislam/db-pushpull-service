from database import Base

from .mixins.auth_mixin import StatusMixin
from .mixins.leave_application import EmpLeaveApplication, LeaveApplication


class OracleLeaveApplication(LeaveApplication, StatusMixin, Base):

    __tablename__ = "TB_T_LEAVE_APPLICATION"
    __table_args__ = {"schema": "HRMS"}

    def __repr__(self):
        return f"OracleLeaveApplication(LAID={self.LAID},\
            LAEmpCode={self.LAEmpCode},\
                LID={self.LID})"


class MSSqlLeaveApplication(LeaveApplication, StatusMixin, Base):

    __tablename__ = "TB_T_LEAVE_APPLICATION"

    def __repr__(self):
        return f"MSSqlLeaveApplication(LAID={self.LAID},\
            LAEmpCode={self.LAEmpCode},\
                LID={self.LID})"


class OracleEmpLeaveApplication(
    LeaveApplication, EmpLeaveApplication, StatusMixin, Base
):

    __tablename__ = "TB_T_EMP_LEAVE_APPLICATION"
    __table_args__ = {"schema": "HRMS"}

    def __repr__(self):
        return f"OracleEmpLeaveApplication(LAID={self.LAID},\
            LAEmpCode={self.LAEmpCode},\
                LID={self.LID})"


class MSSqlEmpLeaveApplication(
    LeaveApplication, EmpLeaveApplication, StatusMixin, Base
):

    __tablename__ = "TB_T_EMP_LEAVE_APPLICATION"

    def __repr__(self):
        return f"MSSqlEmpLeaveApplication(LAID={self.LAID},\
            LAEmpCode={self.LAEmpCode},\
                LID={self.LID})"
