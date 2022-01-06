

# A lambda function to sort list of names based on the last name
scifi_authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C.Clarke',\
                 'Frank Herbert', 'Orson Scot Card', 'Douglas Adams', 'H. G. Wells']
scifi_authors.sort(key= lambda name: name.split(' ')[-1].lower())