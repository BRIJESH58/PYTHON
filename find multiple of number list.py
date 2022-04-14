"""
WRITE A PROCEDURE TO FIND MIN, MAX, MEAN, STANDARD DEVIATION, VARIANCE OF NUMBER LIST.
"""

import statistics

List = [10, 50, 80, 70, 49, 23, 11, 4]

minimum = min(List)
maximum = max(List)
mean = statistics.mean(List)
standard_deviation = statistics.pstdev(List)
variance = statistics.variance(List)

print(minimum, maximum, '%.2f'%mean, '%.2f'%standard_deviation, '%.2f'%variance)