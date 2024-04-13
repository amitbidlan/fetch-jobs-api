class JobTypeNotFoundException(Exception):
    def __init__(self, job_type):
        super().__init__(f"Job type '{job_type}' not found.")
class GetJobCode:
    def getJobCode(job_type):
        job_codes = {
            "part-time job":"emc_07",
            "full-time employee":"emc_04",
            "contract employee":"emc_03",
            "temporary employee":"emc_02",
            "other":"emc_05"
        }

        job_code = job_codes.get(job_type)
        if job_code is None:
            raise JobTypeNotFoundException(job_type)
        return job_code
