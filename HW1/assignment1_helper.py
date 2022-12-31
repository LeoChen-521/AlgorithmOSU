import assignment1

'''
    This file contains helper functions for assignemnt1.  You should not need to edit
    this file, except for the last line when you test your algorithm.

    I will use <python3> to run this code.
'''


def run_majority_party_size(input_file_path, output_file_path):
    global __delegate_parties, __number_of_delegates, __number_of_queries

    with open(input_file_path) as infile:
        __delegate_parties = [int(x) for x in infile.readline().split()]
        __number_of_delegates = len(__delegate_parties)
        __number_of_queries = 0

        with open(output_file_path, 'w') as outfile:
            outfile.write(
                '{} {}'.format(
                    str(
                        assignment1.majority_party_size(
                            __number_of_delegates,
                            same_party
                        )
                    ),
                    str(__number_of_queries)
                )
            )
def same_party(x, y):
    global __number_of_queries
    __number_of_queries += 1

    if x < 0 or y < 0 or x >=__number_of_delegates or y>=__number_of_delegates:
        return None
    return __delegate_parties[x] == __delegate_parties[y]


'''
    To test your function, you can fill the following command with the the input/output
    files paths that you want to read from/write to.  Then, you implement <majority_party_size>
    in the assignment1.py.
'''
run_majority_party_size('test00.in', 'test00.out')
