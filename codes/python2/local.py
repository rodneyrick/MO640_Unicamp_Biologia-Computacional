############################################
##UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO##
##BIOLOGIA COMPUTACIONAL                  ##
##VITOR ROLIM                             ##
##ALINHAMENTO GLOBAL - NEEDLEMAN          ##
############################################

def createMatrix(A,B):
    '''cria e preenche uma matriz de i linhas e j colunas'''
    matrix = []
    count=0
    for i in A:
        matrix.append([])
        for j in B:
            matrix[count].append(None)
        if(count==(len(A)-1)):
            return matrix
        else:
            count+=1

def penalty(x,y):
    '''penalizacao da comparacao dos pares 1 para match, -1 para mismatch, -2 para gap'''
    if(x==y):
        return 1
    elif(x!=y and (x=="-" or y=="-")):
         return -2
    else:
         return -1

def finalScore(A,B):
    '''calcula o score final do alinhamento consultando a funcao finalScore'''
    i=len(A)
    count=0
    for element in range(0,i):
        count+=penalty(A[element],B[element])
    return count
    
def align(A,B):
    '''alinha duas sequencias'''
        
    #Cria a matriz F e define o valor do gap
    F=createMatrix(A,B)
    #GAP
    d=-2
        
    #preenchendo a primeira linha da matriz F
    for i in range(len(A)):
        F[i][0] = d*i
    #preenchendo a primeira coluna da matriz F
    for j in range(len(B)):
        F[0][j] = d*j
        
    #preenchendo as outras posicoes da matriz F com o maior valor entre as cedulas de cima, esquerda e diagonal.
    for i in range(1,len(A)):
        for j in range(1,len(B)):
            choice1 = F[i-1][j-1] + penalty(A[i-1],B[j-1])
            choice2 = F[i-1][j] + d
            choice3 = F[i][j-1] + d
            F[i][j] = max(choice1,choice2,choice3,0)

    AlignmentA=""
    AlignmentB=""

    i=len(A)-1
    j=len(B)-1
    #alinhando as sequencias A,B
    while(i>0 and j>0):
        print 'A=', AlignmentA
        print 'B=', AlignmentB
        
        #calcula os scores da posicao atual e de seus vizihos. Comecando da ultima posicao da matriz.
        score = F[i][j]
        scoreDiag = F[i-1][j-1]
        scoreUp = F[i][j-1]
        scoreLeft = F[i-1][j]
        
        if(score==scoreDiag + penalty(A[i-1],B[j-1])):
            if(AlignmentA=="" and AlignmentB==""):
                AlignmentA = A[i]+AlignmentA
                AlignmentB = B[j]+AlignmentB              
            AlignmentA = A[i-1]+AlignmentA
            AlignmentB = B[j-1]+AlignmentB
            i = i-1
            j = j-1
        elif(score==scoreLeft + d):
            AlignmentA = A[i-1]+AlignmentA
            AlignmentB = "-"+AlignmentB
            i = i-1
        elif(score==scoreUp + d):
            AlignmentA = "-"+AlignmentA
            AlignmentB = B[j-1]+AlignmentB
            j = j-1
        elif(score==0):
            AlignmentA = A[i]+AlignmentA
            AlignmentB = B[j]+AlignmentB
            # j = j-1
    while(i>0):
        AlignmentA = A[i-1]+AlignmentA
        AlignmentB = "-"+AlignmentB
        i = i-1
    while(j>0):
        AlignmentA = "-"+AlignmentA
        AlignmentB = B[j-1]+AlignmentB
        j = j-1
        
    return AlignmentA,AlignmentB,finalScore(AlignmentA,AlignmentB)


print align('ABRACADABRA', 'CABECADECABRA')