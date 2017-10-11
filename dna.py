__author__ = 'emorgan'


def base_frequency(strand):
    """return frequency of dna base occurrence

    DNA is made up of four bases: guanine (G), adenine (A), thymine (T), or cytosine (C)
    this function analyzes a DNA strand and returns a report of the number of times each base occurs

    >>> base_frequency("AAAACCCGGT")
    'guanine (G):2, adenine (A):4, thymine (T):1, cytosine (C):3'

    >>> base_frequency("ACGT")
    'guanine (G):1, adenine (A):1, thymine (T):1, cytosine (C):1'

    >>> base_frequency("acgt")
    'guanine (G):1, adenine (A):1, thymine (T):1, cytosine (C):1'
    """
    strand = strand.upper()
    G = strand.count("G")
    A = strand.count("A")
    C = strand.count("C")
    T = strand.count("T")

    return 'guanine (G):{}, adenine (A):{}, thymine (T):{}, cytosine (C):{}'.format(G, A, T, C)
    
def reverse_strand(strand):
    """returns the reverse compliment of a strand

    >>> reverse_strand("AAAACCCGGT")
    'ACCGGGTTTT'

    >>> reverse_strand("aaaacccggt")
    'ACCGGGTTTT'

    """
    reverse = strand.upper()[::-1]
    rc = []
    for letter in reverse:
        if letter == 'A':
            rc.append('T')
        if letter == 'T':
            rc.append('A')
        if letter == 'G':
            rc.append('C')
        if letter == 'C':
            rc.append('G')       
    

    return "".join(rc)
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
