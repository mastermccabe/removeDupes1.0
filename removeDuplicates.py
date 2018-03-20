
def removeDups(immutableString):
    tempString = []
    for x in immutableString:
        tempString.append(x)

    tempString.sort()

    returnList = []
    newString = ''
    for i in tempString:
        if i not in returnList:
            returnList.append(i)
            newString = ''.join(returnList)


    return newString



string = "geeksforgeeksasdfbsadfjkdsfjksdjfksjdfksjdkfjskdfjskdjfksjdfk"
print removeDups(string)
