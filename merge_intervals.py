# [[1,4],[6,7],[5,6]] --> [[1,4],[6,7]]
# start with first, except this will take n^2 time
# if we implement sorting then we can drop below n^2 (linear)
# take first one and compare sorted starts and compare neighbors

def merge_intervals(input_intervals):
    # input_intervals.sort() ???

    result = []
    start, end = input_intervals[0]
    for i in range(1,len(input_intervals)):
        if end >= input_intervals[i][0]:
            end = max(end, input_intervals[i][0])
        else:
            result.push([start,end])
    result.push([start, end])
