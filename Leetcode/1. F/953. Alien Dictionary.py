# https://leetcode.com/problems/verifying-an-alien-dictionary/
def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dictionary = { i:order.index(i) for i in order}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            iteration_length = min(len(word1), len(word2))
            for j in range(iteration_length):
                if word1[j] != word2[j]:
                    if order_dictionary[word1[j]] > order_dictionary[word2[j]]:
                        return False
                    else:
                        break
                else:
                    continue
            else:
                if len(word1) > len(word2):
                    return False
        return True
