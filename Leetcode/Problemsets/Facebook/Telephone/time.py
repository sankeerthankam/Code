def reorderLogFiles(self, logs: List[str]) -> List[str]:
  ll = []
  ld = []

  for ele in logs:
      # list of strings for every elememt
      lele = ele.strip().split(" ")

      if re.match("^[a-zA-Z]+$", lele[1]):
          ll.append(lele)
      else:
          ld.append(" ".join(lele))

  print(ll)


  ll = [" ".join(i) for i in sorted(ll, key = lambda x: x[1:])]



  print(ll)

  return ll + ld
