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

## C functions in Python

In Python 3, it is possible to run functions from other languages.
`pqcrypto` library is written in C.

Compile the source code in directory `src/` and load it in Python:

```bash
cd src/
make c_func.so
```

```python
import ctypes

# Load the library
c_func = ctypes.CDLL("src/c_func.so")
# Define data types
c_func.ADD.argtypes = [ctypes.c_int, ctypes.c_int]

# Run the function
result: int = c_func.ADD(4, 3)
```

**Useful**:
* [ctypes documentation](https://docs.python.org/3/library/ctypes.html)
* [Calling C Functions from Python](https://www.journaldev.com/31907/calling-c-functions-from-python)
* [How to Call a C function in Python](https://www.geeksforgeeks.org/how-to-call-a-c-function-in-python/)

### Ex. 1 (1p)

- Use file `ex1.py` and `src/c_func.c`.
- Add subtraction function (`SUB`) into the C source code, compile the code and use it in Python code.

```c
void SUB (int num_1, int num_2, int *result) {}
```

- Call the function in Python:

```python
c_func.SUB(...)
# Hint: To pass a pointer to a file, you must create an instance of the object
#       and then pass the reference. Look into the documentation of `ctypes`.
```

Test it for inputs:
- 126, 53
- 37, 94

## PQC NIST schemes

Create virtual environment.
It will create new root path for Python to install packages into, to prevent polluting your user directory:

```bash
sudo apt install python3-venv
python3 -m pip install venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install wheel
```

Ensure your editor/IDE will use this virtual environment:

- VSCode
  - CTRL+SHIFT+P > Python: Select Interpreter > .venv/bin/python3
  - Open `.vscode/settings.json` and add `"python.terminal.activateEnvironment": true`
- PyCharm
  - Settings > Project > Interpreter > .venv/bin/python3

To enter the virtual environment manually (e.g. in terminal), run

```bash
source .venv/bin/activate
```

---

Install library [pqcrypto](https://github.com/kpdemetriou/pqcrypto) mentioned above:

```bash
python3 -m pip install pqcrypto
```

If the automatic installation fails, follow the manual steps:

```bash
# download latest release from https://pypi.org/project/pqcrypto/#files
tar --extract -f pqcrypto-0.1.3.tar.gz
cd pqcrypto-0.1.3/
python3 setup.py install --prefix $ABSOLUTE_PATH_OF_VENV_DIRECTORY
# wait until it is installed
```

The package should now be importable

```python
from pqcrypto.kem.saber import encrypt, decrypt
```

### Ex. 2 (1p)

- Use file `ex2.py`.
- Compare execution time and size of security entities for different functions from pqcrypto:
  - three KEM schemes,
  - three signing schemes.
- Make sure they have the same security level.
  - See more about security levels on [nist.gov](https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization/evaluation-criteria/security-(evaluation-criteria)).
  - See the security levels of pqcrypto functions on [openquantumsafe.org](https://openquantumsafe.org/liboqs/algorithms).
- Measure and compare execution time of each scheme (e.g., https://stackoverflow.com/a/7370824).
- Measure and compare the size of keys and other entities (e.g., `len(public_key)`).

### Ex. 3/HW 1 (1p)

- Install library `sympy`.
  - E.g. by running `python3 -m pip install sympy`.
- Complete the function `ntt` in `ex3.py`.
- Test your implementation by running `pytest test.py::test_ntt`.
- Complete the function `innt` in `ex3.py`.
- Test your implementation by running `pytest test.py::test_intt`.
