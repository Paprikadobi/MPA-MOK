# Laboratory 4 - PQC

In this laboratory we will work with *pqcrypto* library which implements some of the [PQC NIST candidates to be standardized and round 4 finalists](https://csrc.nist.gov/News/2022/pqc-candidates-to-be-standardized-and-round-4) listed below:  

**Candidates to be standardized**
| Public-Key Encryption/KEMs  | Type | Security Level | Pk + Sk + Ct [B] | 
| ------------- | ------------- | ------------- | ------------- |
| **CRYSTALS-Kyber** | lattice | 128  | 1 568 |


| Digital Signatures  | Type | Security Level | Pk + Sk + Sgn [B] | 
| ------------- | ------------- | ------------- | ------------- |
| **CRYSTALS-Dilithium**  | lattice | ~128  | 4 173 |
| Falcon | lattice | 128  | 2 435 |
| SPHINCS  | hash | 128  | 17008 |

**Round 4**
| Public-Key Encryption/KEMs  | Type | Security Level | Pk + Sk + Ct [B] | 
| ------------- | ------------- | ------------- | ------------- |
| Classic McEliece  | code | 128  | 267 700 |
| BIKE | code | 128 | 8337 |
| HQC  | code | 128 | 9019 | 
| SIKE | synergy | 128 | 688 |


Kyber and Dilithium belong to Cryptographic Suite for Algebraic Lattices (CRYSTALS), and both rely on the hardness of MLWE problem. 


## How to run C function in python3

In python3, it is possible to run functions from other languages. 
*pqcrypto* lib uses C programs, let us try to run a C funtion in python3. 

```python
import ctypes, os

⋮

# do to src folder and compile C source
system_output = os.system("cd src && make")
# load .so
CFUNC = ctypes.CDLL("src/libCFunctionFile.so")
# define data types
CFUNC.SUM.argtypes = [ctypes.c_int, ctypes.c_int]

# run c function
python_sum = CFUNC.SUM(python_num_1, python_num_2)

⋮
```

---
HINT: see [example.py](example.py) and [src/](src)

---

**Useful**:
* [ctypes](https://docs.python.org/3/library/ctypes.html)
* [Calling C Functions from Python](https://www.journaldev.com/31907/calling-c-functions-from-python)
* [How to Call a C function in Python](https://www.geeksforgeeks.org/how-to-call-a-c-function-in-python/)

### Ex. 1 (1p)
* create another C function 
```c
void sub(int num_1, int num_2, int *result)
```
* function compute **num_1 - num_2**
  * NOTE: that is void function, result goes throught pointer int *result
* use this function in python, show the result

## PQC NIST schemes

Lib [pqcrypto](https://github.com/kpdemetriou/pqcrypto) mentioned before

```console
pip3 install pqcrypto
```

<details>
  <summary>Troubleshooting</summary>
  
  **Solution - manual install:**
  
  * install virtualenv
  ```console
  pip3 install virtualenv
  ```
  * `cd` into directory with all labs
  * create virtual environment (virtualenv might not be in the $PATH variable, search for it):
  ```console
  virtualenv venv
  # or
  <PATH_TO_VIRTUALENV.EXE> venv
  ```
  * make sure your IDE uses new environment:
  * in VSCode:
  * CTRL+SHIFT+P -> "Python: Select Interpreter" -> ./venv/bin/python
  * this should create .vscode folder with settings.json, open it
  * there should already be `"python.pythonPath": "<RELATIVE_PATH_TO_VENV/BIN/PYTHON(.EXE)>"` setting, add comma and this line:
  * `"python.terminal.activateEnvironment": true`
  * now, every new terminal opened should have virt. env. activated
  * `(venv)` is at the start the line
  * [Download](https://pypi.org/project/pqcrypto/#files) pqcrypto-0.1.3.tar.gz
  * unpack pqcrypto-0.1.3.tar.gz into root directory
  * (maybe winrar portable on windows?)
  * `cd` into unpacked "pqcrypto-0.1.3" directory
  * run install script with correct prefix and wait few minutes
  ```console
  % python3 setup.py install --prefix=<INSERT_ABSOLUTE_PATH_OF_VENV_FOLDER>
  ```
  * pqcrypto now should be installed and usable with `from pqcrypto.XXX.XXX import encrypt, decrypt`
  * NOTE: you might to install again other used libraries again (such as numpy, etc.)
  * make sure to have activated virt. env. when using `pip install XXX`


  Credits: **Petr Muzikant**
</details>

---

### Ex. 2 (1p)
* compare execution time and size of security entities for different implementations of functions from pqcrypto
   * compare at least 3 KEM schemes
   * compare at least 3 signing schemes
* they have to be in the same security level to have a valid comparison, more about [security levels](https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization/evaluation-criteria/security-(evaluation-criteria))
* measure and compare the execution time of each scheme - [timeit](https://docs.python.org/3/library/timeit.html). Check also [this](https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python)
* measure and compare the size of security entities (Memory [B]) - use len(byte_object)

---

### Ex. 3/HW. 1 (1p)

* create function `ntt` that will convert polynomial to NTT domain
* **input**: *p*, *alpha*, *q*, *n*
  * *p* - polynomial that should be converted
  * *alpha* - subgroup generator of degree *n*
  * *q* - coefficient modulus
  * *n* - degree of polynomial
* **output**: NTT representation of polynomial

Test it with this parameters:  
```python
p = [3, -1, 1, 0]
alpha = 2
q = 5
n = 4
```
Output should be: `[3, 0, 0, 4]`

---

HINT: use `numpy.polynomial.polynomial.polyval` to evaluate polynomial.

---

* create function `intt` that will convert polynomial from NTT domain
* **input**: *p_ntt*, *alpha*, *q*, *n*
  * *p_ntt* - NTT representation of polynomial
  * *alpha* - subgroup generator of degree *n*
  * *q* - coefficient modulus
  * *n* - degree of polynomial
* **output**: polynomial

Test it with same parameters, for *p_ntt* use output from `ntt` function.

To solve modular equations install `sympy` library and use following code.
```python
from math import gcd
from sympy import Matrix

'''
Solve system of modular equations.

:param A: Matrix (NxN) representing coefficients of variables.
:param B: Matrix (Nx1) representing evaluations of polynomial.
:param q: Coefficient modulus.

:return: Matrix(Nx1) represeting coefficients of polynomial.
'''
def solve(A: Matrix, b: Matrix) -> Optional[Matrix]:
    det = int(A.det())

    if gcd(det, q) == 1:
        return pow(det, -1, q) * A.adjugate() @ b % q
    else:
        print("cannot solve this equation")
```