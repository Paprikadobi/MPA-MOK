import ctypes

# Load the library
c_func = ctypes.CDLL("src/c_func.so")
# Define data types
c_func.ADD.argtypes = ctypes.c_int, ctypes.c_int
c_func.ADD.restype = ctypes.c_int

# Run the function
add_1: int = c_func.ADD(4, 3)
print(f"[PY] Result = {add_1}")
