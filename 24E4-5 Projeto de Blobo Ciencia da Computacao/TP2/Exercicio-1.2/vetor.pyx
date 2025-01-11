import numpy as np
from cython.parallel import prange

def soma_serial(long[:] inp):
  cdef long i, size
  cdef long out
  size = inp.shape[0]
  out = 0
  with nogil:
    for i in prange(size):
      out += inp[i]
  return out
