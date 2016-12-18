import itertools as it

# SEQUENCES = ['AGG', 'AGT', 'CCG', 'CGT', 'GAG', 'GGA', 'GGT', 'GTA', 'GTG', 'TAG', 'TGG']

AATCCCGATGATCCGATCGAGTATCGTAGA
# AATCGATCCGATCGATCGTAGA

SEQUENCES = ['AAAAAA','ACGATCA','GTACAGTA','CAGTGG','AGGGCC','CCCCCCC','CAGTTTTT','CGGTTTTT']
LONGEST_SUPERSTRING = ''.join(SEQUENCES)

def find_shortest_superstring():
    current_shortest = LONGEST_SUPERSTRING
    trim = len(current_shortest)-1
    seen_prefixes = set()
    for perm in it.permutations(SEQUENCES):
        candidate_string = ''.join(perm)[:trim]
        if candidate_string in seen_prefixes:
            continue
        seen_prefixes.add(candidate_string)
        while is_superstring(candidate_string):
            current_shortest = candidate_string
            candidate_string = candidate_string[:-1]
            trim = len(current_shortest)-1
    return current_shortest

def is_superstring(s):
    return all(seq in s for seq in SEQUENCES)

def main():
    print 'Searching for shortest superstring containing all strings.'
    ss = find_shortest_superstring()
    print 'Found shortest superstring containing all strings:\n{}'.format(ss)

if __name__ == '__main__':
    main()