def threeNumZero(A):
    A.sort()
    for i in range(0, len(A)-2):
        j = i + 1
        k = len(A)-1
        while(j < k):
            if( A[i] + A[j] + A[k] == 0):
                print( "Zero at:", A[i],A[j],A[k])
                return True
            elif (A[i]+A[j]+A[k] < 0):
                j += 1
            else:
                k -= 1
    print("no zero's")
    return False

A = [1, 4, 45, 6, 10, 8, -5]

threeNumZero(A)
