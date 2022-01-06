#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number
def unknownScale(x):
    return lambda n: n*x

#Write a Python program to sort a list of tuples using Lambda.
grade_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
grade_tuples.sort(key= lambda item: item[1])

# A lambda function to sort list of names based on the last name
scifi_authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C.Clarke',\
                 'Frank Herbert', 'Orson Scot Card', 'Douglas Adams', 'H. G. Wells']
scifi_authors.sort(key= lambda name: name.split(' ')[-1].lower())