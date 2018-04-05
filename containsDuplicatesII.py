def containsDuplicatesII(arr, k):
    # sort array
    arr.sort()
    # set 2 pointers
    i = 0
    j = 1
    count = 0
    # 1, 4, 5, 6, 9
    # i = 1
    # j = 4
    #  3
    while (i < len(arr)):
        if (arr[i] - arr[j] <= k):
            count += 1
            i += 1
            j += 1
        else:
            i += 1


    return count

arr = [1, 5, 4, 6, 9]
k = 1
print ("Count of pairs within k is ", containsDuplicatesII(arr, k))


# ---*---*---*---*---*---*---*---*---*---*---*---*---*---*
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
