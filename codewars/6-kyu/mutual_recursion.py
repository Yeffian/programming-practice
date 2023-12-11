f_cache = dict()

def female(num):
      global f_cache
      if num in f_cache:
        return f_cache[num];
      else:
        res = 1 
        if num > 0:
             res = num - male(female(num-1))
        f_cache[num] = res
        return res

m_cache = dict()
def male(num):
      global m_cache
      if num in m_cache:
        return m_cache[num];
      else:
        res = 0 
        if num > 0:
             res = num - female(male(num-1))
        m_cache[num] = res
        return res
