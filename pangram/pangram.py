def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in alphabet:
            return False
        return True
