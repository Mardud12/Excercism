def find_anagrams(word, candidates):
    result = []
    for i in candidates:
        if len(word) != len(i):
            continue
        else:

            if sorted(list(i.lower())) == sorted(list(word.lower())) and i.lower() != word.lower():
                result.append(''.join(i))

            else:
                continue
    return result
