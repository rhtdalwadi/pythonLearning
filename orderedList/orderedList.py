# orderednums.py
#
# Extracts a list of integers from a text file, one per line
# and creates an ordered list using the insert() method.

# Start with an empty list.
theList = []

theFile = file("orderedList/values.txt", "r")
for line1 in theFile:
    num = int(line1)
    print "line", line1
    print "num", num
    # Find the proper position of the item.
    i = 0
    while i < len(theList) and num > theList[i]:
        i = i + 1

        # Insert the item.
    theList.insert(i, num)

theFile.close()
print theList
