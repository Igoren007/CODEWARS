#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
#
#Example
#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice



def duplicate_count(text):
    count = 0
    list_sym = []
    text = text.lower()
    for pos, sym in enumerate(text):
        c1 = text[0:pos]
        c2 = text[pos+1:]
        if (sym in c1 or sym in c2) and (sym not in list_sym):
            count += 1
            list_sym.append(sym)
    return count
            

print(duplicate_count("aabBcde"))