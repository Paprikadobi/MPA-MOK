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
    # select only rows containing number and given language
    filtered_data: np.ndarray[str] = data[np.logical_and(data[:, 0] == 'NR', data[:, 1] == lang)]

    # slice only numbers and convert them to float
    year_counts = filtered_data[:, 4:].astype(np.float32)

    return year_counts.sum(axis=0)

if __name__ == '__main__':
    data = load_dataset()

    print(list(students_per_year(data, 'CZE')))