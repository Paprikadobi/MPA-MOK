from typing import List
from ex1 import load_dataset

import numpy as np
import matplotlib.pyplot as plt

def statistics(data: np.ndarray[str], langs: List[str]) -> tuple[dict[str, np.ndarray[np.float32]], dict[str, np.ndarray[np.float32]]]:
    """ Extracts *nr* and *pc* datasets from dataset.

    :param data: Full dataset loaded using `load_dataset` function.
    :param langs: List of languages to extract.
    :return: Tuple of dictionaries representing *nr* and *pc* datasets
    """
    nr_data: np.ndarray[str] = data[data[:, 0] == 'NR']
    pc_data: np.ndarray[str] = data[data[:, 0] == 'PC']

    nr_dict, pc_dict = {}, {}

    for lang in langs:
        nr_dict[lang] = nr_data[nr_data[:, 1] == lang, 4:].astype(np.float32).sum(axis=0)
        pc_dict[lang] = pc_data[pc_data[:, 1] == lang, 4:].astype(np.float32).sum(axis=0)

    return nr_dict, pc_dict

def plot_bar(data: dict[str, np.ndarray[np.float32]], langs: List[str]):
    """ Plots bar chart for year 2019 of provided dataset.

    :param data: Dictionary representing dataset, generated using `statistics` function.
    :param langs: List of languages to plot.
    """
    values = []

    for lang in langs:
        values.append(data[lang][0])

    plt.xticks(rotation=90)
    plt.bar(langs, values)
    plt.show()

def plot_bars(data: dict[str, np.ndarray[np.float32]], langs: List[str]):
    """ Plots bar chart for year 2019 of provided dataset comparing with anonymized one.

    :param data: Dictionary representing dataset, generated using `statistics` function.
    :param langs: List of languages to plot.
    """
    generalized_data = generalize(data)
    values, generalized = [], []

    for lang in langs:
        values.append(data[lang][0])
        generalized.append(generalized_data[lang][0])

    plt.subplot(1, 2, 1)
    plt.yscale('log')
    plt.xticks(rotation=90)
    plt.bar(langs, values, 0.4, label='raw')
    plt.subplot(1, 2, 2)
    plt.yscale('log')
    plt.xticks(rotation=90)
    plt.bar(langs, generalized, 0.4, label='generalized')
    plt.show()

def generalize(data: dict[str, np.ndarray[np.float32]]) -> dict[str, np.ndarray[np.float32]]:
    """Generalize value in a bigger category.

    :param data: Dictionary representing dataset, generated using `statistics` function.
    :return: Generalized dataset in same format as input dataset.
    """
    result = {}
    breaks = [1e3, 1e5, 1e7, 1e9]

    for lang in data:
        result[lang] = np.array(data[lang])

        for i in range(len(data[lang])):
            for b in breaks:
                if b >= data[lang][i]:
                    result[lang][i] = b
                    break

    return result

if __name__ == '__main__':
    data = load_dataset()

    attrs = np.transpose(data)

    langs = sorted(list(set(attrs[1])))
    langs.remove('TOTAL')
    langs.remove('OTH')

    nr_data, pc_data = statistics(data, langs)

    plot_bars(nr_data, langs)