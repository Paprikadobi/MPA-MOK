# Laboratory 2 - Numpy library and Lattice

NumPy (Numerical Python) is an open-source Python library used for working with numerical data. Numpy allows working with array and matrix data structures over modulus which is exactly what we need for lattices. 

**Install dependencies(libs)**
  ```console
  $ pip3 install <dep_name>
  ```
  - depends on what default python uses
  ```console
  $ pip3 install <dep_name>
  ```
  - eg. install *numpy*:
  ```console
  $ pip3 install numpy
  ```
**Import to python file**
  - whole library
  ```python
  import numpy
  ```
  - whole library (shorter way)
  ```python
  import numpy as np
  ```
  - specific function
  ```python
  from <lib_name> import <fce>
  from <lib_name> import <fce> as <imported_fce_name>
  ```
  - advanced imports check [this](https://realpython.com/python-import/)

## List vs Array

Arrays and lists can be of integers, strings, and floats. In this lesson, we will consider the integer case while we will work with strings when we will deal with data anonymization.

Vectors and NxN matrices are 1-dimension and N-dimension arrays, respectively. (We will consider squared matrices)

A normal list of elements can be created as:
```python
list = [0,1,2,3,4,5]
```
try to apply modulus 3 to the list:
```python
list % 3
```
The difference between a list and an array is that **the array is a list with assigned properties**, i.e. we can do more “crypto” operations with an array.

Let us see what happens with np.array():

*  The following command allows you to create a vector of those specific 6 elements.
```python
v = np.array([0,1,2,3,4,5])
```
*  Try to apply modulus 3 to the vector:
```python
mod_vect = v % 3 
```
* You can see that modulus 3 is applied to each element of the array. Use the following command to see the value of a variable:
```python
print(mod_vect)
```
  ---
  You can also have access to each element of an array. Try:
  ```python
  mod_vect[0] 
  mod_vect[6]
  ```
  the last command gives you an error since `mod_vect` has only 6 elements.
  
  ---

## Vectors and Matrices

The difference between a vector and a matrix is the dimension:

**Vector**
* Create the vector:
```python
v = np.array([0,1,2,3,4,5,6,7]) 
```
* Try these commands (The first prints the number of element of the array, the second the dimension of the array. Vectors are 1-dimension array, i.e. a list of elements):
```python
v.size
v.ndim
```

**Matrix**
* Let us create a 2-dimension matrix, i.e. an array of arrays, and apply the same commands:
```python
matrix = np.array([[0,1,2,3],[4,5,6,7]]) 
matrix.size 
matrix.ndim
```

---
Note that the vector and the matrix have the same number of elements but different dimension:
```python
matrix[0] 
matrix[0][1]
```
The first shows you a vector, the second an element.  

---

## Random Number Generator

One way to create a lattice (NxN matrix) is to generate it at random. For testing purposes, we may need to generate always the same matrix, therefore we need a random number generator with a seed.  

* We inizialize the generator with seed 6, for instance:
```python
np.random.seed(6)
```
* We want a vector with 5 elements which are integers mod 11 , therefore:
```python
np.random.randint(low=-10, high=11, size=5) 
```
* We want a 3x3 matrix of integers mod 11, therefore:
```python
np.random.randint(low=-10, high=11, size=(3,3))
```

## Ex. 1 (0.5p)
Let *M* be NxN matrix and *v* a vector with N elements. In a file, create a function with:
* **input** (three integers): *seed*, *dim* and *mod*, where *dim* represents the dimension of M and the size of v
* generate *M* and *v* at random modulus mod and print their values
* compute *c* = M*v modulus mod
* **output** c 

---
**Hint**: Is the output a matrix or a vector? 
The output has to be a vector.  
Please check the difference between M*v and M.dot(v) 

---

## Lattice – Good and Bad bases

A good basis allows finding the solution to the Closest Vector Problem (CVP), a bad basis gives a wrong solution. Goldreich-Goldwasser-Halevi (GGH) algorithm is based on it.

---
**Note**: It is easy to derive a bad basis from a good one while it is hard vice versa.  

Therefore, we create a good basis which is a matrix L, then we compute a bad one by multiplying L with U. U is a matrix with det = +- 1 and dimension equal to the one of L.

---

We will use [lattice.py](lattice.py) file with pre-defined functions:
* hamdamard_ratio() 
* rand_unimod() 
* babai() 

**Example**:
* Import lattice as lt
* Consider/define a good base L = [[2,0,0],[1,1,0],[0,0,3]] 
* Check if it is a good basis  (hamdamard ratio has to be bigger than 0.7) 
  * **Hint**: lt.hamdamard_ratio() 
* Build a 3x3 matrix U with determinant equal to +- 1 
  * **Hint**: lt.rand_unimod()
* Compute a bad base B = LU  
  * **Hint**: check the command np.matmult() 
* Check that the hamdamard ratio of B is close to 0 (smaller than 0.3)  
* If it is not, change the seed and find another B 

---
**Solution**:

```python
import numpy as np
import lattice as lt
L = np.array([[2, 0, 0], [1, 1, 0], [0, 0, 3]])  
lt.hamdamard_ratio(L) 
U = lt.rand_unimod(3) 
B = np.matmul(L, U) 
lt.hamdamard_ratio(B) 
```

![Example.png](Example.png)

---

Now we have a good base, namely L, and a bad one, namely B. 
We can try to apply Babai’s Closest Vertex Algorithm.

---
**IMPORTANT**: A = np.array([[5,0],[1,2]]) is different from B = np.array([[5,1],[0,2]]).  
In particular, we have that A = np.transpose(B). 
Note that we consider the case A = [b1,b2] where b_1 = [5,0] and b_2 = [1,2] are the vectors of the basis.  

---

## Ex. 2 (0.7p)
1. Define a function *distance_lattice_vector* with:
  * Input: basis, v
  * Compute CVP using Babai algorithm to vector v using the lattice basis
    * **Hint**: `babai` function is defined in [lattice.py](lattice.py)
  * print CVP (Babai output)
  * Compute the distance between b (Babai output) and v try with `dist = np.linalg.norm(np.abs(v - b))` the more the vectors are close, the more the norm is small
  * Ouput: dist
2. Define a fuction with:
  * Input: basis1, basis2, v  
  * Compute distance for basis1 and basis2 
  * Check which distance is smaller 
  * Print the result commenting which basis gives the best result.  
  * Output: -1 if basis1 is better, 1 if basis2 is better, 0 if both have same distance
3. Run the second function on L and B that you computed above and one of the below vectors as possible input for v: 
  * v1 = [-5,1,0]
  * v2 = [-10,1,13] 

---
**Q**: Which result is closer to v?  
**Q**: Is v in L? 

---

## Ex. 2.1 - graphical representation of Ex. 2 (0.8p)
* Use EX. 2 output as starting point
* Use source code from https://asecuritysite.com/encryption/lattice_plot, modify it for our use case (2d -> 3d)
* Show Latice with base vectors, vector v and output of Babai alg. (b)
  * v in different color as base vectors
  * also vector to b point in different color

## Ex. 3/ Hw. 1 (1p)
In [ggh_plain.py](ggh_plain.py) file, you can find the implementation of GGH cryptosystem. Create a function that print GGH while the program is executed, “Alice computes ...” and “Bob computes ...”. In particular: 
* Alice - key generation 
* private key and its Hamdamard ratio 
* public key and its Hamdamard ratio 
* Unimodular matrix  
* Bob - encryption 
* message 
* ciphertext 
* Alice - decryption 
* message

## References
* [numpy - Vectors and Matrices](https://numpy.org/doc/1.21/user/absolute_beginners.html)
* [numpy - Random Numbers Generators](https://numpy.org/doc/stable/reference/random/generator.html )
* [GGH](https://github.com/EdwardMork/GGH-CryptoSystem )
