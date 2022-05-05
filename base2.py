def dec_to_bin(x, n=10):
  """
  Computes x in base 2 up to n digits of mantissa.
  """
  
  s = f'{bin(int(x))[2:]}.'
  x -= int(x)
  for _ in range(n):
    x *= 2
    s += str(int(x >= 1))
    x -= int(x >= 1)
  return s
