def create_paths_and_alignments_for_global_alignment(i, j, s_aligned, t_aligned):
    if (i > 0):
        if (j > 0):
            up = A_global[i-1][j] + g
            diag = A_global[i-1][j-1] + (M if s[i - 1] == t[j - 1] else m)
            down = A_global[i][j-1] + g
            paths_here = [A_global[i][j] == up, A_global[i][j] == diag, A_global[i][j] == down]
            paths_global[i][j] = paths_here
            
            if (paths_here[0]):
                create_paths_and_alignments_for_global_alignment(i - 1, j, s[i - 1] + s_aligned, '-' + t_aligned)
            
            if (paths_here[1]):
                print(t[j - 1] , t_aligned)
                create_paths_and_alignments_for_global_alignment(i - 1, j - 1, s[i - 1] + s_aligned, t[j - 1] + t_aligned)
            
            if (paths_here[2]):
                create_paths_and_alignments_for_global_alignment(i, j - 1, '-' + s_aligned, t[j - 1] + t_aligned)
            
        else: # j == 0
            paths_global[i][j] = [True, False, False]
            create_paths_and_alignments_for_global_alignment(i - 1, j, s[i - 1] + s_aligned, '-' + t_aligned)
            
    elif (j > 0):
        paths_global[i][j] = [False, False, True]
        create_paths_and_alignments_for_global_alignment(i, j - 1, '-' + s_aligned, t[j - 1] + t_aligned)
        
    else:           
        paths_global[i][j] = [False, False, False]
        alignments_global.append([s_aligned, t_aligned])
        
        

s = "CGC"
t = "GCAGGT"

M = 1
m = -1
g = -2

# considerando o A_global ja preenchido, e a matriz paths_global preenchida vazia quando o A_global foi preenchido
A_global = [
    [0, -2, -4, -6, -8, -10, -12], 
    [-2, -1, -1, -3, -5, -7, -9], 
    [-4, -1, -2, -2, -2, -4, -6], 
    [-6, -3, 0, -2, -3, -3, -5]
]

paths_global = [
    [[False, False, False]] * (len(t) + 1) for i in range(len(s) + 1)
]
print(paths_global)

alignments_global = []
create_paths_and_alignments_for_global_alignment(len(s), len(t), '', '')

# for i in paths_global:
#     print(i)
#     print()

for i in alignments_global:
    print(i[0])
    print(i[1])
    print()