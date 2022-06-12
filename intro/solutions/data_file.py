"""
===================
I/O script example
===================

Script to read in a column of numbers and calculate the min, max and sum.

Data is stored in data.txt.
"""

def load_data(filename):
    with open(filename) as fp:
        data_string = fp.read()
    # Could instead use the following one line with list comprehensions!
    # data = [float(x) for x in data_string.split()]
    return [float(x) for x in data_string.split()]

if __name__ == '__main__':
    data = load_data('data.txt')
    # Python provides these basic math functions
    print('min: %f' % min(data))
    print('max: %f' % max(data))
    print('sum: %f' % sum(data))
