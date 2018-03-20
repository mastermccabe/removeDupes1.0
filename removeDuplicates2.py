def removeDups(string):
    temp = []
    sortedString = ''
    for x in string:
        if x not in temp:
            temp.append(x)
            
    sortedString = ''.join(temp)

    # temp.sort()

    return sortedString


string = "geeksforgeeksasdfbsadfjkdsfjksdjfksjdfksjdkfjskdfjskdjfksjdfk"
print removeDups(string)
