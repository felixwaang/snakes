#wondrous function, returns x/2 if even, and 3*x + 1 if odd.
#Felix Wang

def wondrous(x):
  while(x != 1):
    if(x % 2 == 0):
      print(x)
      return x/2
      
    else:
      print(x)
      return 3*x + 1
      
