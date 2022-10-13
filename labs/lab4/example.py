import ctypes, os

# do to src folder and compile C source
system_output = os.system("cd src && make example.so")
# load .so
clib = ctypes.CDLL("src/example.so")
# define data types
clib.add.argtypes = [ctypes.c_int, ctypes.c_int]

res = clib.add(5, 3)

print(f'[PYTHON] result = {res}')