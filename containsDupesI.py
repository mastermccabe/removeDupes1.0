# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


def containsDuplicate(nums):
    print(len(nums) > len(set(nums)))
    return len(nums) > len(set(nums))


nums = [1,2,3,4,5,6,1]
containsDuplicate(nums)
