def removeDups(string):
    temp = []
    sortedString = ''
    for x in string:
        if x not in temp:
            temp.append(x)

    # temp.sort()
    sortedString = ''.join(temp)



    return sortedString


string = "geeksforgeeksasdfbsadfjkdsfjksdjfksjdfksjdkfjskdfjskdjfksjdfk"
print removeDups(string)
