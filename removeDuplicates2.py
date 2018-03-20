def removeDups(string):
    # convert to list
    temp = []
    for x in string:
        if x not in temp:
            temp.append(x)


    # temp.sort()

    return temp


string = "geeksforgeeksasdfbsadfjkdsfjksdjfksjdfksjdkfjskdfjskdjfksjdfk"
print removeDups(string)
