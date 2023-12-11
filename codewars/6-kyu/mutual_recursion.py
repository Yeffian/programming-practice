f_cache = dict()

def f(num):
      global f_cache
      if num in f_cache:
        return f_cache[num];
      else:
        res = 1 
        if num > 0:
             res = num - m(f(num-1))
        f_cache[num] = res
        return res

m_cache = dict()
def m(num):
      global m_cache
      if num in m_cache:
        return m_cache[num];
      else:
        res = 0 
        if num > 0:
             res = num - f(m(num-1))
        m_cache[num] = res
        return res
