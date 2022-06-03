# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words.
#     You should return an array of all the anagrams or an empty array if there are none. For example:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
# Note for Go
# For Go: Empty string slice is expected when there are no anagrams found.

def anagrams(word, words):
    output = []
    for w in words:
        if len(w) == len(word):
            count = 0
            for letter in set(w):
                if letter in set(word):
                    count += 1
            if count == len(set(w)) == len(set(word)):
                output.append(w)
    return output


if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
    print(anagrams('laser', ['lazing', 'lazy', 'lacer']))
    print(anagrams('aabb', ['aabb', 'bbaa', 'abab', 'baba', 'baab', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']))