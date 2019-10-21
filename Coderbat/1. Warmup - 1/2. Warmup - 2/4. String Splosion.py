# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  new_str = ''
  for i in range(len(str)+1):
    if i == 0:
      pass
    else:
      new_str = new_str + str[:i]
  return new_str
