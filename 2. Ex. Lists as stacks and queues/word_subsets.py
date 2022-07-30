class Solution:

"""Suppose for example:

words1 = ['food', 'coffee', 'foofy']
   words2 = ['foo', 'off']

Here's the plan:
  1) Construct a dict in which the key is a char in
     one or more words in words2, and the key's max
     count in those words.
           for 'foo': c2 = {'o': 2, 'f': 1}
           for 'off': c2 = {'o': 1, 'f': 2}
           so: d = {'o': 2, 'f': 2}

  2) Use a counter for each word in words1 to determine
     whether the word has at least the quantity of each char
     in d:
           for 'food'  : c1 = {'o': 2, 'f': 1, 'd': 1} (fails at 'f')
           for 'coffee': c1 = {'f': 2, 'e': 2, 'o': 1} (fails at 'o')
           for 'foofy ': c1 = {'f': 2, 'o': 2, 'y': 1} (success)

  3) return answer:
           answer = ['foofy'] """

def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    d, ans = defaultdict(int), []

    for word in words2:  # <-- 1)
        c2 = Counter(word)
        for ch in c2:
            d[ch] = max(d[ch], c2[ch])

    for word in words1:  # <-- 2)
        c1 = Counter(word)

        for ch in d:
            if c1[ch] < d[ch]: break
        else:
            ans.append(word)  # <-- else executes only if the for-loop
            #      completes without break

    return ans  # <-- 3)