# Import a counter object to keep track of counts
# For each element in the list, split the string to extract the count and domains
  # For each extracted domains, update the count in counter object for each domain combination i.e. "['.'.join(domains[i:])]"
# Return the result in accepted format.

Use an 
class Solution:
    def subdomainVisits(self, ls: List[str]) -> List[str]:
        from collections import Counter
        c = Counter()
        for i in ls:
            count, *domains = i.replace(" ",".").split(".")
            for i in range(len(domains)):
                c['.'.join(domains[i:])] += int(count)
        return [" ".join((str(v), k)) for k, v in c.items()]
