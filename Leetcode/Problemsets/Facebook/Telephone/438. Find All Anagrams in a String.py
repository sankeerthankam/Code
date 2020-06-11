# Approach 1
# Works for most of the testcases but does for edge cases where the substring is overlapping.

def findAnagrams(s, p):
  import itertools
  import re
  ls = []
  for i in itertools.permutations(p):
      i = ''.join(i)
      if i in s:
          l = [i.start() for i in re.finditer(i, s)]
          ls.extend(l)
  return list(set(ls))
  
# Approach 2
# Add comments

def findAnagrams(s, p):
  n = len(s)
  m = len(p)

  p = Counter(p)                    # Convert list of anagram letters to a Counter (hashtable)
  ans = []

  window = None
  for i in range(0,n-m+1):
      if i == 0: 
          window = Counter(s[:m])   # Initialize window with beginning of s => length = length of anagram letters
      else:    
          window[s[i-1]] -= 1       # Move window to right: 1. remove character on the left
          window[s[i+m-1]] += 1     #                       2. add character on the right
      if len(window - p) == 0:      # Check if window is anagram (direct comparison of counters does not work with 0 entries)
          ans.append(i)

  return ans


# Approach 3
# Add comments

def findAnagrams(s, p):
  myDictP=collections.Counter(p)
  myDictS=collections.Counter(s[:len(p)])
  output=[]
  i=0
  j=len(p)

  while j<=len(s):
      if myDictS==myDictP:
          output.append(i)

      myDictS[s[i]]-=1
      if myDictS[s[i]]<=0:
          myDictS.pop(s[i])

      if j<len(s):    
           myDictS[s[j]]+=1
      j+=1
      i+=1

  return output 

def findAnagrams(s, p):
