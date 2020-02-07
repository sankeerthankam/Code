# Remove the punctuation and convert the words to lowercase in the paragraph
# Use Counter from collections and sort the counter object (desc)
# Loop through the counter object -> Check if it belongs to banned words -> else return the word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter
        paragraph = paragraph.lower().strip()
        paragraph = re.sub('[^a-z0-9]+', ' ', paragraph)

        word_counts = Counter(paragraph.split(' '))

        for i, j in word_counts.most_common():
            if i not in banned:
                return i
