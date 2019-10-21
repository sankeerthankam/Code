# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def sub_list(string):
  ls = []
  for i in range(len(string)):
    if i+1 == len(string):
      break
    else:
      ls.append(string[i:i+2])
  return ls
  
def string_match(a, b):
  a_lst, b_lst = sub_list(a), sub_list(b)
  return len(set(a_lst).intersection(set(b_lst)))
  
