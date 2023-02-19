from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    """
    Create a small sample of jobs
    """
    jobs = [
        {
            "title": "Maquinista",
            "min_salary": 2000,
            "max_salary": 3000,
            "date_posted": "2022-12-20",
        },
        {
            "title": "Analista de Software",
            "min_salary": 4000,
            "max_salary": 5000,
            "date_posted": "2022-12-22",
        },
        {
            "title": "Motorista",
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2022-12-23",
        },
        {
            "title": "Auxiliar administrativo",
            "min_salary": 1700,
            "max_salary": 2500,
            "date_posted": "2022-12-24",
        },
    ]

    """
    Sort the jobs by different criteria and check the result
    """
    sort_by(jobs, "min_salary")
    assert [job["title"] for job in jobs] == [
        "Auxiliar administrativo",
        "Maquinista",
        "Motorista",
        "Analista de Software",
    ]

    sort_by(jobs, "max_salary")
    assert [job["title"] for job in jobs] == [
        "Analista de Software",
        "Motorista",
        "Maquinista",
        "Auxiliar administrativo",
    ]

    sort_by(jobs, "date_posted")
    assert [job["title"] for job in jobs] == [
        "Auxiliar administrativo",
        "Motorista",
        "Analista de Software",
        "Maquinista",
    ]

    """
    Check that jobs without valid values for chosen criteria appear at end
    """
    jobs[1]["max_salary"] = None
    sort_by(jobs, "max_salary")
    assert [job["title"] for job in jobs] == [
        "Analista de Software",
        "Maquinista",
        "Auxiliar administrativo",
        "Motorista",
    ]
