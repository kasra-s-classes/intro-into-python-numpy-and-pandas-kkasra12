import itertools
import os
import random
from string import ascii_lowercase

import numpy as np
import pandas as pd
from python_questions_answers import (
    average_monthly,
    column_average,
    find_missing,
    list_comprehension,
    permutation,
    simulate_data_saver,
    sort_dataframe,
    sort_rows,
    steps_to_one,
)


def test_permutation0():
    assert sorted(permutation("a")) == ["a"]


def test_permutation1():
    assert sorted(permutation("ab")) == ["ab", "ba"]


def test_permutation2():
    assert sorted(permutation("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]


def test_permutation3():
    string = "".join(random.choices(ascii_lowercase, k=8))
    assert sorted(permutation(string)) == sorted(
        set(["".join(i) for i in itertools.permutations(string)])
    )


def test_find_missing0():
    assert find_missing(["a", "b", "c", "d", "f"]) == "e"


def test_find_missing1():
    assert find_missing(["O", "Q", "R", "S"]) == "P"


def test_find_missing2():
    max_len = 10
    letters = ascii_lowercase[
        (s := random.randint(0, len(ascii_lowercase) - max_len)) : s + max_len
    ]
    assert len(letters) == max_len, f"{letters=}, {max_len=}, {s=}"
    missing_letter_index = random.randint(1, max_len - 2)
    print()
    missing_letter = letters[missing_letter_index]
    letters = letters[:missing_letter_index] + letters[missing_letter_index + 1 :]
    assert find_missing(letters) == missing_letter


def test_steps_to_one():
    nums_and_answers = [
        (948, 36),
        (312, 37),
        (194, 119),
        (130, 28),
        (185, 44),
        (406, 40),
        (653, 25),
        (163, 23),
        (919, 129),
        (421, 40),
    ]
    for num, answer in nums_and_answers:
        assert steps_to_one(num) == answer


def test_list_comprehension():
    for _ in range(3):
        lst = []
        lst.extend(list(ascii_lowercase))
        lst.extend(list(range(100)))
        random.shuffle(lst)
        assert list_comprehension(lst) == [
            i for i in lst if isinstance(i, int) and i % 2 == 0
        ]


def test_buffer():
    if os.path.exists("data"):
        os.remove("data")
    simulate_data_saver()
    with open("data", "r") as f:
        data = f.read().splitlines()
    assert data == [str(i) for i in list(range(100))]


def test_column_average():
    for _ in range(3):
        array = np.random.rand(10, 10)
        print(array)
        assert np.allclose(column_average(array), np.mean(array, axis=0))


def test_sort_rows():
    for _ in range(3):
        array = np.random.rand(10, 10)
        index_col = random.randint(0, 9)
        assert np.allclose(
            sort_rows(array, index_col), array[np.argsort(array[:, index_col])]
        )


def test_sort_dataframe():
    df = pd.read_csv("data.csv")
    df_out, n = sort_dataframe(df.copy(), "date")
    df["date"] = pd.to_datetime(df["date"])
    df_diff = df["date"].diff()
    omit_indices = df_diff[df_diff < pd.Timedelta(0)].index
    df = df.drop(omit_indices)
    assert n == len(omit_indices)
    print(df_out.dtypes)
    print(df.dtypes)
    assert df_out.equals(df)


def test_average_monthly():
    df = pd.read_csv("data.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month
    assert df.groupby("month")["values"].mean().equals(average_monthly(df))
