import numpy as np

def load_dataset() -> np.ndarray[str]:
    # read data set by lines
    with open('edu.txt', 'r') as file:
        lines = file.readlines()

    data = []

    for line in lines[1:]:
        data.append(line.replace(':', '0').split())

    return np.array(data)

def students_per_year(data: np.ndarray[str], lang: str) -> np.ndarray[np.float32]:
    """Count the total number of students per year.

    :param data: Data set loaded from 'edu.txt' file.
    :param lang: Language acronym (e.g. CZE).
    :return: List of students studying given language.
    """
    # TODO: Complete the code here