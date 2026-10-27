import numpy

def reshape_rows(values, width):
    if (len(values) % width)!=0:
        return []
    return numpy.asarray(values).reshape(-1,width).tolist()

def block(matrix, rows, columns):
    matrix = numpy.asarray(matrix)
    return matrix[np.ix_(rows, columns)].round(6).tolist()

def column_means(matrix):
    if len(matrix)==0:
        return []
    matrix = numpy.asarray(matrix)
    return numpy.round(numpy.mean(matrix,axis=1), 6).tolist()

def column_range(matrix, column):
    if len(matrix)==0:
        return 0.0
    matrix = numpy.asarray(matrix)
    data = matrix[:,column]
    print(data)
    return round(data.max() - data.min(), 6)

print('aaa')
print(column_range([[1, 2], [5, 7]], 1))
