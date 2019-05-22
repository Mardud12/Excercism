def proteins(strand):

    import re

    s = re.findall('...', strand)

    protein = []



    for x in s:
        if x == 'UAA' or x == 'UAG' or x == 'UGA':

            break

        elif x == 'AUG':
            protein.append('Methionine')

        elif x == 'UUU' or x == 'UUC':
            protein.append('Phenylalanine')

        elif x == 'UUA' or x == 'UUG' :
            protein.append('Leucine')

        elif x == 'UCU' or x == 'UCC' or x == 'UCA' or x == 'UCG':
            protein.append('Serine')

        elif x == 'UAU' or x == 'UAC':
            protein.append('Tyrosine')

        elif x == 'UGU' or x == 'UGC' :
            protein.append('Cysteine')

        elif x == 'UGG':
            protein.append('Tryptophan')


        else:
            break

    return protein


