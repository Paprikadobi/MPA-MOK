import ctypes

# Load the library
c_func = ctypes.CDLL("src/c_func.so")
# Define data types
c_func.ADD.argtypes = ctypes.c_int, ctypes.c_int
c_func.ADD.restype = ctypes.c_int
c_func.SUB.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)
c_func.SUB.restype = None

# Run the function
add_1: int = c_func.ADD(4, 3)
print(f"[PY] Result = {add_1}")

sub_1 = ctypes.c_int()
c_func.SUB(126, 53, ctypes.byref(sub_1))
print(f"[PY] Result = {sub_1.value}")

sub_2 = ctypes.c_int()
c_func.SUB(37, 94, ctypes.byref(sub_2))
print(f"[PY] Result = {sub_2.value}")
