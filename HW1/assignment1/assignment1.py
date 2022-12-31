'''
    This file contains the template for Assignment1.  You should fill the
    function <majority_party_size>.  The function, recieves two inputs:
      (1) n: the number of delegates in the room, and
      (2) same_party(int, int): a function that can be used to check if two members are
      in the same party.

    Your algorithm in the end should return the size of the largest party, assuming
    it is larger than n/2.

    I will use <python3> to run this code.
'''


def majority_party_size(n, same_party):
    '''
        n (int): number of people in the room.
        same_party (func(int, int)): This function determines if two delegates
            belong to the same party.  same_party(i,j) is True if i, j belong to
            the same party (in particular, if i = j), False, otherwise.

        return: The number of delegates in the majority party.  You can assume
            more than half of the delegates belong to the same party.
    
    '''

    # Replace the following line with your code.
    maj_index, count, size = 0, 0, 0
    
    #Handle the special cases
    if 1 <= n <= 2:
        return n
    
    #Look for the index of the majority elements
    for i in range(n):
        if count == 0:
            maj_index = i
            count = 1
            
        elif same_party(maj_index, i):
            count += 1
            
        else:
           count -= 1
    
    #Count the size of the majority Party
    for i in range(n):
        if same_party(maj_index, i):          
            size += 1
    
    return size