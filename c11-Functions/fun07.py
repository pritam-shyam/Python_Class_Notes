sample1 = [1, 2, 3, 4, 5]
sample2 = [10,11,12,13,14]
sample3 = [8,8,3,2]

def stat_summary(x):
    maxx = max(x)
    minx = min(x)
    n = len(x)
    sum_x = sum(x)
    avg = sum_x / n
    deviations = [(a - avg)**2 for a in x]
    variation = sum(deviations)/n
    std_deviation = variation ** .5
    return({'max': maxx, 'min': minx, 'n': n, 'sum': sum_x,
            'avg': avg, 'variance': variation, 'stdev': std_deviation})

print(stat_summary(sample1))
print(stat_summary(sample2))
print(stat_summary(sample3))
