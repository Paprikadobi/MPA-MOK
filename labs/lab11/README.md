# Laboratoty 11 - Data Anonymization

**Data anonymization** allows protecting private data while publishing useful information.
It is based on *Statistical Disclosure Control (SDC)* methods that aim at releasing data that preserve their
statistical validity while protecting the privacy of each data subject.

In this laboratory, we will work with **non-perturbative masking**. 

| Method  | Numerical data | Categorical data |
| ------------- | ------------- | ------------- |
| Sampling  |  | x |
| Global recoding | x | x |
| Top and bottom coding | x | x |
| Local suppression |  | x |

## The dataset 

The [Adult Education Survey (AES)](https://ec.europa.eu/eurostat/web/microdata/adult-education-survey) covers adult participation in education and training and is one of the main data sources for EU lifelong learning statistics. 
We will use as input [EDU](edu.txt) dataset which is a sub-dataset of AES that covers the topic *Pupils by education level and modern foreign language studied - absolute numbers and % of pupils by language studied*. 
The database is publicly available in [Eurostat](https://ec.europa.eu/eurostat/web/education-and-training/data/database) web page. 

The dataset structure is as shown in this table.

| Unit of measure  | Language | International standard | Geopolitical entity | 2019 | 2018 | 2017 | 2016 | 2015 | 2014 | 2013 | 2012 
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Number (NR) | CZE | Primary education (ED1) | Germany (GE) |  |  |  |  |  | |  |  |
| Percentage (PC) | ENG | Lower secondary education (ED2 | Estonia (EE)  |  |  |  |  |  | |  |  |
|  | GER | Upper secondary education (ED3) | France (FR) |  |  |  |  |  | |  |  |
|  | ITA | Upper secondary education - general (ED34) | Portugal (PT)  |  |  |  |  |  | |  |  |
|  | ... | Upper secondary education - vocational (ED35) | ...  |  |  |  |  |  | |  |  

The sub-survey counts 29 Languages, 37 Geopolitical entities and it was ran for 8 years (from 2012 to 2019). 

## Statistical analysis on the uploaded dataset

First the dataset needs to be loaded. You can use the function `load_dataset` defined in [ex1.py](ex1.py).

```python
data = load_dataset()
```

We would like to run some statistical analysis on `data`. Below are some useful commands.  

- The dataset is upload in records, i.e., `data[i]` is a record (row) for all `i`. We may need to work on attributes (columns). 
we can use the function `np.transpose`

```python
import numpy as np
attrs = np.transpose(data)
```

-  We would like to know the selection of Language acronyms appearing in the dataset. We can use the function `set` which let you pass from a list with repetition to a set. In sets, each element appear only once.

```python
langs = set(attrs[1])
len(langs)
```

- In order to have the list of languages, we need to remove *TOTAL* or *OTH* (other). 

```python
langs.remove('TOTAL') 
langs.remove('OTH') 
```

- Therefore, the number of luanguages consisidered is `len(langs)` and the acronyms are:

```python
['ARA', 'BUL', 'CHI', 'CZE', 'DAN', 'DUT', 'ENG', 'EST', 'FIN', 'FRE', 'GER', 'GLE', 'GRE', 'HRV', 'HUN', 'ITA', 'JPN', 'LAV', 'LIT', 'MLT', 'POL', 'POR', 'RUM', 'RUS', 'SLO', 'SLV', 'SPA', 'SWE', 'UNK']
```

- To pass from set to list: 
```python
langs_list = list(langs)
```

### Exercise 1 (1p)
Create a python function that counts the totoal number of students per year (*2019*, *2018*, *2017*, *2016*, *2015*, *2014*, *2013*, *2012*).   
Fill in the missing code in `students_per_year` function in [ex1.py](ex1.py) file.

*Hint*: you are interested only in values belonging to *NR*.

### Datasets to be anonymized
From data we can extract two datasets *nr* and *pc*. 
- *nr* is the dataset with the total number of students studying that language per year
- *pc* is the dataset with the percentage of students studying that language per year

To create this datasets use `statistics` function defined in [ex2.py](ex2.py). It will return two dictionaries with following structure.

```python
{
	'UNK': array([536704. , 721953.8, 396938. , 482828. , 458536. , 487764. ,
       473634. ,   3440. ], dtype=float32), ...
}
```


To plot data from the dataset use `plot_bar` function.
This plot helps in recognizing "dangerous" values (too big in particular). 

## Data privacy - non-perturbative masking

Some languages present few students and other can be recognized for the opposite situation. 
Let use apply Global Recoding method to the dataset *nr*. 

### Exercise 2 (1 p) 
Propose an anomization of *nr* by:
- identifying unsecure values (too small, too big)
- generalizing the value in a bigger category
- plot the raw data and the anonymized data
- IMPORTANT: consider only the list of languages (remove *TOT*, *OTH*)

### Homework: data needs to be prepared (1 p.)
- choose a dataset that you find interesting
- export the dataset in *cleaned.txt* file
- run some simple statistics of your interest
