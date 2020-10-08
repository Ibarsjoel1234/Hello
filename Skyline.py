# Source = Udemy

def myfunc(x):
  out = []
  for i in range(len(x)):
    if i % 2 == 0:
      out.append(x[i].uppercase())
    else:
      out.append(x[i].lowercase())
  return ''.join(out)
  
  
 myfunc('ABCDEFGHIJKLMNOPQRSTUVWXYZ)
