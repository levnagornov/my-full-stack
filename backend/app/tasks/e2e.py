from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from typing import Any


class V_ENV(Enum):
    OA2 = "OA2"
    OA3 = "OA3"
    
@dataclass
class TaskResult:
    is_successful: bool
    stdout: str
    log: bytes
    data: dict[str, Any] = {}
    
class Task:
    def __init__(self, env: V_ENV, test_title: str, reporting_date: datetime, static_data_implementation_date: datetime):
        self.env: V_ENV = env
        self.test_title: str = test_title
        self.reporting_date: datetime = reporting_date
        self.static_data_implementation_date: datetime = static_data_implementation_date

    def dry_run(self, static_data_implementation_date: datetime, sd_files: list[str]) -> TaskResult:
        # call .sh
        # get vxsdu.log or Wai's log
        return TaskResult(
            is_successful=True,
            stdout="grep INFO /.../dry_run.log",
            log="",
            data={"affected_tables": "Table_1 Table_2"}
        )

    def __create_full_sd_backups() -> TaskResult:
        # get affected tables
        # run e2e.create_sd()
        pass
    
    def __curve_generation() -> TaskResult:
        pass
    
    def __run_sd_transfer() -> TaskResult:
        pass

    def __stop_all_processes() -> TaskResult:
        pass
    
    def __start_all_processes() -> TaskResult:
        pass
        
    def commit_run(self, static_data_implementation_date: datetime, sd_files: list[str]):
        self.dry_run()
        # create_full_sd_backups()
        # commit here...
      
    def validate_sp2xml(reporting_date: datetime, systems: list[str]) -> TaskResult:
        pass
      
    def load_sp(reporting_date: datetime, systems: list[str]) -> TaskResult:
        # insert into preprocessor queue
        # add to tracker?
        pass

    def recalculate(reporting_date: datetime, systems: list[str]) -> TaskResult:
        # insert into vre queue
        # add to tracker?
        pass
    
    def start_vpp() -> TaskResult: 
        # insert into ...
        # check vpp is running
        # add to tracker?
        pass
    
    def start_vde() -> TaskResult:
        # insert into ...
        # check vde is running
        # share export files? 
        # add to tracker?
        pass
    
    def create_rtf_tables(suffix: str, repoting_date: datetime, systems: list[str]) -> TaskResult:
        # create sd tables
        # create tables using rtf tool
        # rename or should be fixed by PSI?
        pass
    
    # idea: track applied SD in the env
    # - revert_sd will reset the tracker
    # - commit_sd will a record to tracker
    # applie_sd_table
    def revert_sd() -> TaskResult:
        pass
    
    # not a task?
    def get_env_info():
        pass
    
    # idea: receive p sp files via xfb from VOM
    def archive_sp_files(systems: list[str], reporting_date: datetime) -> TaskResult:
        pass
        
    def share_sp_file_on_sharepoint():
        pass 


def main():
    task = Task(V_ENV.OA2, "Onboarding XYZ - OA2B")
    result = task.dry_run(datetime(2025, 6, 30), ["test.xlsx"])
    print(result.is_successful)

if __name__ == "__main__":
    main()
