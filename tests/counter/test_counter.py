# import io
from src.pre_built.counter import count_ocurrences


def test_count():
    count_python = count_ocurrences("data/jobs.csv", "python")
    assert count_python == 1639

    count_js = count_ocurrences("data/jobs.csv", "javascript")
    assert count_js == 122
