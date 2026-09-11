import numpy as np
import time
import dust as dst

# 1. Setup 1,000,000 elements
data_list = [1.0] * 1_000_000
data_arr = np.array(data_list)

# Wrap inside Dust Column
dust_col = dst.Column(data_arr)

# 2. Plain Python Sum
t0 = time.perf_counter()
py_sum = sum(data_list)
t1 = time.perf_counter()

# 3. Dust Pipeline Sum
t2 = time.perf_counter()
dust_sum = dust_col >> dst.Sum()
t3 = time.perf_counter()

py_time = t1 - t0
dust_time = t3 - t2

print(f"Python Total: {py_sum} | Time: {py_time:.6f}s")
print(f"Dust Total:   {dust_sum} | Time: {dust_time:.6f}s")
print(f"Dust is ~{py_time / dust_time:.2f}x faster on 1 Million elements!")