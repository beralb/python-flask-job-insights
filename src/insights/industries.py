from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_object = read(path)
    unique_industries_list = []
    for job in jobs_object:
        if (
            job["industry"] not in unique_industries_list
            and job["industry"] != ""
        ):
            unique_industries_list.append(job["industry"])
    print(unique_industries_list)
    return unique_industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filter_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_by_industry.append(job)
    return filter_by_industry
