def removeDups(string, string2):
    # b = set(string2)
    a = set(string.lower())
    b = set(string2.lower())
    return ''.join(a ^ b)
    # - a but not in b, a | b OR, a & b AND, XOR


# string2 = raw_input("Enter second string: ")
string = "abcabcabcABCABC"
string2 = "asdfasdf"
print removeDups(string, string2)
