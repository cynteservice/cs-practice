import numpy

def make_hours():
    return numpy.arange(0,22,3).tolist()

def vector_report(values):
    values = values.copy()
    new_dict ={
    "third": values[2],
    "last": values[-1],
    "middle": values[2:6],
    "every_second": values[::2],
    "reversed": values[::-1],
    }
    return new_dict

def change_vector(values):
    values = numpy.array(values.copy())
    values[2:min(5, len(values))] = 99
    values[::2]=-1
    return values

def cap_above(values, limit):
    values = numpy.array(values)
    values[values>limit] = limit
    values = values.tolist()
    return values


def celsius_to_fahrenheit(values):
    values = [x*9/5+32 for x in values]
    return values

print(change_vector([10, 20, 30, 40, 50]))
