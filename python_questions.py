import os
import pickle
from typing import Any

import numpy as np
import pandas as pd


def permutation(string: str):
    """
    In this question, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

    Create as many "shufflings" as you can!

    Examples:

    With input 'aabb':
    Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    """
    pass


def find_missing(lst: list[str]):
    """
    Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
    You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
    If there is no missing letter, the function should return `None`.
    """
    pass


def steps_to_one(start_num: int):
    """
    we want to make a series of numbers, each series is created like this:
    if the number is even, divide it by 2, if it's odd, multiply it by 3 and add 1.
    we want to know how many steps it takes to get to 1.

    for example, if we start with 3, we get the following series:
    3, 10, 5, 16, 8, 4, 2, 1
    """
    pass


def list_comprehension(lst: list[Any]):
    """
    Given a list of integers, write a one-liner Python list comprehension to generate a new list that contains
    only the even numbers from the original list. note that there may be non-integer elements in the list.
    """
    pass


class Buffer:
    def __init__(self, filename, dtypes=None, max_size=10):
        self.filename = filename
        self.dtypes = dtypes
        if max_size < 1:
            raise ValueError("max_size must be greater than 0")
        self.max_size = max_size
        self.data = []

        if not os.path.exists(self.filename):
            self.save()

    def validate(self):
        if self.dtype is None:
            return
        new_data = filter(lambda x: isinstance(x, self.dtype), self)
        self.data = list(new_data)

    def save(self):
        self.validate()
        with open(self.filename, "w") as f:
            pickle.dump(self.data, f)
        self.data = []

    def add(self, data):
        self.data.append(data)
        if len(self) >= self.max_size:
            self.save()


def simulate_data_saver():
    buffer = Buffer("data", dtypes=int, max_size=10)
    for i in range(100):
        buffer += i


def column_average(array: np.ndarray):
    """
    Given a 2D array, return the average of each column as a 1D array.
    """
    pass


def sort_rows(array: np.ndarray, index_col: int):
    """
    Given a 2D NumPy array, write a Python function that sorts the rows of the array based on the values in a specific column. The column index will be provided as a parameter to the function.
    """
    pass


def sort_dataframe(df: pd.DataFrame, date_col: str):
    """
    we have a dataframe that contains two columns, the first column is 'date' and the second column is 'value'.

    in the date column, they supposed to be sorted, but there are some rows that are not sorted. find those rows and omit them.

    also return the number of rows that you omitted.
    """
    pass


def average_monthly(pd: pd.DataFrame):
    """
    we have a dataframe that contains two columns, the first column is 'date' and the second column is 'value'.
    find the average of the values in each month.
    """
    pass


if __name__ == "__main__":
    # use this part to run your code and debug
    pass
