# filter out values that are less than the average
import statistics
values = [1.2, 5, 1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = statistics.mean(values)

print(list(filter(lambda x: x > avg, values)))

# filter out empty data
data = ['', '1', 5, 'hello', '5+6', '', '....']
print(list(filter(None, data)))