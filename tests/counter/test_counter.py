# import io
from src.pre_built.counter import count_ocurrences


def test_count():
    path = "data/jobs.csv"
    word = "developer"
    count_python = count_ocurrences(path, word)

    assert count_python == 1639
