"""
Pyton module to find the length of a continuously repeating pattern in a list of items
"""

def vprint(mystr, verbose):
    """ print when verbose, quiet otherwise """
    if verbose:
        print(mystr)

def find_repeat(the_list, verbose=False):
    """
    Description: find a repeating pattern in the_list

    @args: the_list, verbose=False
    The list to search and the verbosiness required

    Return: length of repeating pattern
            0 if there is no pattern
    """
    vprint(f'\nfinding repeating pattern in list: {the_list}', verbose)

    for pat_len in range(1, int(len(the_list)/2 + 1 )):

        found_pat=True # we start with the positive assumption
        pat_0 = the_list[0:pat_len]

        vprint(f'Try pat_0: {pat_0}', verbose)

        max_pats, remaining = divmod( len(the_list), pat_len) # how many times pat fits in list

        vprint(f'With a length of {pat_len} a maximum of {max_pats} full patterns would fit, \
            with {remaining} items remaining', verbose)

        for rpt in range(1, max_pats ):
            pat_n = the_list[pat_len*rpt:pat_len*(rpt+1)]
            vprint(f'pat_{rpt}: {pat_n}', verbose)
            if pat_0 != pat_n:
                vprint(f'pattern fails in {rpt}th repetition', verbose)
                found_pat = False
                break

        # Finally, is there a tail & if so, does it match as well?

        if found_pat and remaining:
            if verbose:
                print(f'Pattern repeats {max_pats} times, now inspect remainder')
                print(f'Remaining {remaining} items check')
                print( the_list[:remaining] )
                print( the_list[max_pats*pat_len:] )
            if the_list[:remaining] != the_list[max_pats*pat_len:]:
                vprint('candidate fails in trail', verbose)
                found_pat = False

        # If found_pat still true, we found a pattern!

        if found_pat:
            vprint(f'Full pattern match with length {pat_len}!', verbose)
            return pat_len

    vprint('No pattern match!', verbose)
    return 0
