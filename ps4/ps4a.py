# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return sequence

    
    list1=[]
    first=sequence[0]
    sublist=get_permutations(sequence[1:])
    for j in sublist:
        for i in range(len(j)+1):
            if j[0:i]+first+j[i:len(j)] not in list1:
                list1.append(j[0:i]+first+j[i:len(j)])
    return list1
    
    #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'cde'
    print('Input:', example_input)
    print('Expected Output:', ['cde', 'dce', 'dec', 'ced', 'ecd', 'edc'])
    print('Actual Output:', get_permutations(example_input))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    

