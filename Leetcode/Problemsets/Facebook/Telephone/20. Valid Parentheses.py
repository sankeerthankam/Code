def isValid(s):
  ls_dict = {
              '(' : ')',
              '{' : '}',
              '[' : ']'
  }
  visited = []

  if len(s)%2 != 0:
      return False

  for i in s:
      if i in ls_dict:
          visited.append(i)
      else:
          if len(visited) == 0:
              return False
          if i != ls_dict.get(visited.pop()):
              return False
          else:
              continue

  return len(visited) == 0
