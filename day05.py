from collections import Counter
import re

def nice_word(word):

    for bad_letters in ["ab", "cd", "pq","xy"]:
        if bad_letters in word:
            return False

    letters = Counter(word)
    vowel_count = sum([letters[i] for i in ["a", "e", "i", "o", "u"]])

    res = re.search(r'([a-z])\1', word)

    if res and (vowel_count >= 3):
        return True
    else:
        return False

def nice_word2(word):
    rule1 = False
    rule2 = False
    # Repeat string

    for i in range(len(word) - 1):
        a = word[i:i+2]

        if a in word[i+2:]:
            rule1 = True


        if word[i] in word[i+2:i+3]:
            rule2 = True





    return all([rule1, rule2])

with open('data/day_05.txt') as fh:
    words = fh.read().splitlines()


print("Part 1")
results = []
for word in words:
    results.append(nice_word(word))
print(sum(results))

print("Part 2")
results = []
for word in words:
    results.append(nice_word2(word))
print(sum(results))

