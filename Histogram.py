# this program does not works..
def makehistogram(gradeList):
    # Create a 10 element histogram.
    histogram = [0] * 10
    print "abc"
    # Count the number of each grade.
    i = 0
    while i < len(gradeList):
        grade = gradeList[i] / 10
        histogram[grade] += 1
        i += 1

    print "abc", gradeList
    # Return the histogram.
    return histogram
