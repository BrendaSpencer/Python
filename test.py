import camelcase
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

c = camelcase.CamelCase()

txt = "Hello, World!"

print(c.hump(txt))