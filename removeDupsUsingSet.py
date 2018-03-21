
def removeDups(string):
    # b = set(string2)
    a = set(string)
    return ''.join(a)
    # - a but not in b, a | b OR, a & b AND, XOR


# string2 = raw_input("Enter second string: ")
string = "abcabcabcABCABC"
print removeDups(string)
