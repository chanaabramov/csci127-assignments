def greetr(name):
    return "hello " + name+"!"

def sleep_in(weekday, vacation):
  if weekday and vacation == True :
    return True
  if weekday == True:
    return False 
  else :
    return True

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile :
    return True
  else :
    return False

def sum_double(a, b):
  if a==b :
    return (a+b+a+b)
  else :
    return (a+b)

def diff21(n):
  if n<=21:
    return 21-n
  else :
    return (n-21)*2
    


def parrot_trouble(talking, hour):
  if talking == True :
    if hour > 20 or hour < 7 :
      return True 
    else:
      return False
  else :
    return False 
