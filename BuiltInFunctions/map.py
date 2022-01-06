# convert the temperatures in Celsius to Fahrenheit
temp = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Tokyo', 27),\
         ('Los Angeles', 26), ('New York', 28), ('London', 22), ('Beinjing', 32)]


c_to_f = lambda data: (data[0], 9/5*data[1] +32)

print(list(map(c_to_f, temp)))