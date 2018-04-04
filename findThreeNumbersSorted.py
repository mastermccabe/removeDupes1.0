# Time Complexity O(n^2)

# returns true if there is triplet
# with sum equal to 'sum' present
# in A[]. Also, prints the triplet
def find3Numbers(A, arr_size):

    # Sort the elements
    A.sort()

    # Now fix the first element
    # one by one and find the
    # other two elements
    for i in range(0, arr_size-2):


        # To find the other two elements,
        # start two index variables from
        # two corners of the array and
        # move them toward each other

        # index of the first element
        # in the remaining elements
        l = i + 1

        # index of the last element
        r = arr_size-1
        while (l < r):

            if( A[i] + A[l] + A[r] == 0):
                print("Zeros @", A[i], A[l], A[r]);
                return True

            elif (A[i] + A[l] + A[r] < 0):
                l += 1
            else: # A[i] + A[l] + A[r] > sum
                r -= 1

    # If we reach here, then
    # no triplet was found
    return False

# Driver program to test above function
A = [1, 4, 45, 6, 10, 8, -5]
sum = 22
arr_size = len(A)

find3Numbers(A, arr_size)
