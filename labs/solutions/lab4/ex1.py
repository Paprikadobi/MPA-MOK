import ctypes, os

# go to src folder and compile C source
system_output = os.system("cd src && make ex1.so")

# load .so file
clib = ctypes.CDLL("src/ex1.so")

# define function data types
clib.sub.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

res = ctypes.c_int()

# run c function
clib.sub(5, 2, ctypes.byref(res))

print(res)