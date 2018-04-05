def distinctPairsSet(arr, n, k):
    count = 0
    arr.sort()
    # 1,2,3,4,5,6,9
    print(arr)
    r=0 # 1
    l=0

    while (r < len(arr)):

        if(arr[r] - arr[l] == k):
            count += 1
            r += 1
            l += 1
        elif(arr[r] - arr[l] > k):
            l += 1
        else:  #arr[r] - arr[l] < k
            r += 1
    return count


# O(nlogn)

arr = [1, 5, 3, 4, 6, 9]
# 1,2,3,4,5
n = len(arr)
k = 1
print ("count of pairs with given diff is ", distinctPairsSet(arr, n, k))
