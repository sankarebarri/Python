# filter out values that are less than the average
import statistics
data = [1.2, 5, 1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = statistics.mean(data)

print(list(filter(lambda x: x > avg, data)))