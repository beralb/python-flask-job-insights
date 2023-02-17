from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    jobs_object = read(path)
    salaries = []
    for job in jobs_object:
        salary = job["max_salary"]
        if salary.isdigit():
            salaries.append(int(salary))

    return max(salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_object = read(path)
    salaries = []
    for job in jobs_object:
        salary = job["min_salary"]
        if salary.isdigit():
            salaries.append(int(salary))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    try:
        salary = int(salary)
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError("min_salary is greater than max_salary")

        return min_salary <= salary <= max_salary

    except (ValueError, TypeError, KeyError):
        raise ValueError(
            "dict keys min/max_salary not valid int or salary not int"
        )


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs_list = []
    for job in jobs:
        try:
            job_matches_salary_range = matches_salary_range(job, salary)
        except ValueError:
            # print(f"Error: {error}")
            continue
        if job_matches_salary_range:
            filtered_jobs_list.append(job)
    return filtered_jobs_list
