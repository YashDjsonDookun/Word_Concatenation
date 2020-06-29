#!/usr/bin/python3

class Solution(object):
  def findAllConcatenatedWords(self, words):
    # Fill this in.
    self.words = words
    temp = []
    concat_words = []
    for i in range(len(self.words)):
        for j in range(len(self.words)-1):
            if (self.words[j] + self.words[i]) in self.words:
                temp.append(self.words[j] + self.words[i])
    for word in temp:
        if word in self.words:
            concat_words.append(word)
    concat_words.reverse()
    del temp
    return concat_words

input = ['rat', 'cat', 'cats', 'dog', 'catsdog', 'dogcat', 'dogcatrat']
print(Solution().findAllConcatenatedWords(input))
# ['catsdog', 'dogcat', 'dogcatrat']
