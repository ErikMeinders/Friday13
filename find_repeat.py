"""
Module to find a repeating pattern in a list
"""

def find_repeat(the_list):

    """
    find a repeating pattern in a list

    @args: the_list
    The list to search

    Return: length of repeating pattern
    """

    for pat_len in range(1, int(len(the_list)/2 + 1 )):

        found_pat=True # we start with the positive assumption

        pat_1 = the_list[0:pat_len]
        pat_2 = the_list[pat_len:2*pat_len]

        if pat_1 == pat_2:

            # print('[candidate] Pattern found, length is: ', pat_len)

            # Let's see if it repeatsm more than once

            max_pats = int (len(the_list)/pat_len) # how many times pat fits in list

            for rpt in range(2, max_pats ):
                pat_n = the_list[pat_len*rpt:pat_len*(rpt+1)]
                # print(f'pat 1: {pat_1}')
                # print(f'pat n: {pat_n}')
                if pat_1 != pat_n:
                    # print(f'candidate fails in {rpt}th pattern')
                    found_pat = False
                    break

            # Finally, is there a tail & if so, does it match as well?

            remaining = len(the_list) - max_pats*pat_len
            if found_pat and remaining:
                # print(f'Pattern repeats {max_pats} times, now inspect tail')
                # print(f'Remaining {remaining} items check')
                # print( the_list[0:remaining] )
                # print( the_list[max_pats*pat_len:max_pats*pat_len+remaining] )
                if the_list[0:remaining] != the_list[max_pats*pat_len:max_pats*pat_len+remaining]:
                    found_pat = False

            # If found_pat still true, we found a pattern!

            if found_pat:
                return pat_len
    return 0
