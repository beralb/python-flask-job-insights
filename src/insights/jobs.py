from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        jobs_list = []
        input_file = csv.DictReader(file)
        for row in input_file:
            jobs_list.append(row)
    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_object = read(path)
    job_types_list = []
    for jobs in jobs_object:
        if jobs["job_type"] not in job_types_list:
            job_types_list.append(jobs["job_type"])
    return job_types_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
