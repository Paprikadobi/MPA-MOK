# Laboratory 3 - Polynomials and R-LWE problem

NumPy has a package dedicated to polynomials: `numpy.polynomial`.

We need to import the libraries:

```python
import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P
```

**Note**: `P` and `poly` are different:
- `P` allows defining a polynomial. Here a polynomial is represented as an equation.
- `poly` allows making computations on polynomials. Here a polynomial is represented as the vector of its coefficients (array representation).

## Preparing the workspace

Use files `exN.py`, where *N* is the excersise number. Write all your functions there,
and make sure you follow the function names and argument types and orders. You will be
able to run tests that make sure you have implemented the code correctly.

You can run the tests by invoking `pytest` in the lab directory, or by using
integrated pytest in PyCharm or other IDEs.

### ipython3

`ipython3` uses `__repr__` instead of `__str__` by default.
If you want to see pretty math-like equations, run the following after importing the `P` class:

```python
P.__repr__ = P.__str__
```

An ACII-only alternative could be

```python
P.__repr__ = lambda p: " ".join(f"{coef:+}x^{i}" for i, coef in enumerate(p.coef))
```

## Create a polynomial

A polynomial can be created from its coefficients given as a list or numpy array:

```python
p1 = P([1,2,3])
print(p1)
```

Please check the ordering of the coefficients `[1, 2, 3]` with the powers of x: *1 + 2 x + 3 x^2*.

Try:
```python
p = P([2,1,3])
print(p)
```

Given a polynomial `p1`, we can access the coefficients using

```python
print(p1.coef)
```

**Note**: a polynomial can be represented as an equation *1+2x+3x^2* or as an array *[1, 2, 3]*.

Since a polynomial is generated from an array and numpy allows to generate random arrays, we can generate a polynomial at random.
We can try to generate a polynomial of degree 3 at random in Z_11[x]:

```python
coef_poly = np.random.randint(low=-10, high=11, size=3)
p1 = P(coef_poly)
print(p1)
```

Please check [Laboratory 2](https://github.com/xcibik00/MPA-MOK/tree/cibik_readme/labs/lab2) for more details on how to generate an array mod 11 at random.

## Computations with polynomials

We can add, subtract, multiply and divide polynomials:

```python
summed: np.array = poly.polyadd(p1.coef, p2.coef)
subtracted: np.array = poly.polysub(p1.coef, p2.coef)
multiplied: np.array = poly.polymul(p1.coef, p2.coef)
divided: np.array = poly.polydiv(p1.coef, p2.coef)
```

**Note**: the input of the aforementioned functions is the array of coefficients, therefore:
- `p1.coef`: you create `p1 = P([1,2,3])` and then you consider the coeffients of `p1`
- `np.array([1,2,3])`: you directly consider the coefficient "without definining the polynomial"

The command `poly.polydiv(array, array)` can be used for creating the classes of polynomials in *Zp[x]/(p1)*

### Ex. 1 (0.5p)

- Complete the function `polyadd` in `ex1.py`.
- Create a function that tests `polyadd`:
  - Create polynomial *pmod = x^2 + 1*.
  - Generate two polynomials `poly1`, `poly2` of degree five at random with given coefficient modulus.
  - Compute `result1 = polyadd(...)` with coefficient modulus *11*.
  - Compute `result2 = polyadd(...)` with coefficient modulus *5*.
- Test your implementation by running `pytest test.py::test_polyadd`.

### Ex. 2 (0.5p)

- Complete the function `polymul` in `ex2.py`.
- Create a function that tests `polymul`:
  - Create polynomial *pmod = x^2 + 1*.
  - Generate two polynomials `poly1`, `poly2` of degree five at random with given coefficient modulus.
  - Compute `result1 = polymul(...)` with coefficient modulus *11*.
  - Compute `result2 = polymul(...)` with coefficient modulus *5*.
- Test your implementation by running `pytest test.py::test_polymul`.

## R-LWE problem generation

LWE and R-LWE problems roughly say:

> Given *(A, As+e)*, it is hard to compute *s*.

**Note**: LWE uses vectors, R-LWE polynomials.
However, we saw that the problems are "two sides of the same coin", i.e., we can pass from one representation to the other.

In the specification, we have that:
1. *A* and *s* are generated at random,
2. *e* follows the normal distribution,

Below are three ways of generating specific polynomials.

1. We already know how to generate a random vector of integers from the uniform distribution.
   Let *p* be a random polynomial of degree 3 in *Z11[x]*. Therefore, *A* can be generated with the following command:
   ```python
   A = np.random.randint(low=-10, high=11, size=(4,4))
   ```

3. In case of normal distribution, the command is:
   ```python
   e = np.random.normal(0, 2, size=4)
   ```
   Note that this command generates a polynomial with coefficients in a normal distribution of mean 0 and a standard deviation of 2.

4. A binary vector can be generated as follows:
   ```python
   s = np.random.randint(0, 2, size=4)
   ```

## A R-LWE encryption scheme

Now we are able to generate R-LWE and LWE problems.
The following encryption algorithm is based on R-LWE problem and has Homomorphic Encryption (HE) property.

### Ex. 3 - Key Generation (0.5p)

- Complete functions `get_*_polynomial` in `ex3.py`.
- Complete the function `generate_keypair` in `ex3.py`.
- Create a function that uses `generate_keypair`:
  - Hint: Create separate functions for generating binary, uniform and normal polynomials, you will use it later.
  - Complete the function.
  - Display variables 'a', 'b', 'e', 's' for *dimension = 4*, *coefficient modulus = 5*, *polynomial modulus = x^2 + 1*.
- Test your implementation by running `pytest test.py::test_generate_keypair`.

## Encryption algorithm

In order to gain the HE property, we need to do as follows.

- the messagge/plaintext pt is in Zt
- the public key `pk = (a, b)`
- the ciphertext `ct = (ct0, ct1)` is a tuple of two polynomials where
- `ct0 = b * u + e1 + delta * m mod q`
- `ct1 = a * u + e2 mod q`


In particular,
- u is a random binary polynomial
- `delta = q // t`
- m is the constant polynomial m(x) = scaled_pt, where `scaled_pt = delta*m mod q`  
(for example, if scaled_pt = 3, m(x) = 3 and if the polynomials have degree 2, then `m = np.array([3,0,0])`)
- e1 and e2 are polynomials normally distributed

Note: the symbol `//` represents the integer division in python language.

### Ex. 4 - Encryption (0.5p)

- Complete the function `encrypt` in `ex4.py`.
- Create a function that uses `encrypt`:
  - Complete the function.
  - Display the ciphertext for input *dimension = 4*, *coefficient modulus = 6481*, *polynomial modulus = x^4 + 1*; the choice of the other parameters is up to you.
- Test your implementation by running `pytest test.py::test_encrypt`.

### Ex. 5 or homework (1p)

The scheme has homomorphic encryption properties:  
Let *a* be an integer in *Zt*, *ct = Enc(pt)* a ciphertext and *ct'= Enc(pt')* another ciphertext, write a code that checks:

- `Dec(a + Enc(pt)) = Dec(Enc(pt+a))`
- `Dec(Enc(pt) + Enc(pt')) = Dec(Enc(pt+pt'))`
- `Dec(a*Enc(pt)) = Dec(Enc(pt*a))`

Use the following parameters:

- *dimension* any integer,
- *degree = 2^4*,
- *coefficnet modulus = 2^15*,
- *message modulus = 2^8*,
- *polynomial modulus = `P([1] + [0] * (degree - 1) + [1])`*;
- *a* any integer,
- *message1* any integer,
- *message2* any integer.

File `ex5.py` already contains functions for adding and multiplying.

## References

- [numpy documentation on polynomials](https://numpy.org/doc/stable/reference/routines.polynomials.html)
- [Regev and LWE in Python](https://gist.github.com/youben11/f00bc95c5dde5e11218f14f7110ad289)
- [Article "Somewhat Practical Fully Homomorphic Encryption"](https://eprint.iacr.org/2012/144.pdf)
