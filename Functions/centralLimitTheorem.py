import random

def central_limit_theorem(pop, n):
    '''
    Parameters
    ----------
    pop : List of population
    n : Sample size

    Returns: The average of the sample
    '''
    sample = []
    for i in range(n):
        sample.append(random.choice(pop))

    return sum(sample)/ len(sample)



        